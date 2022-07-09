"""
Get SC Labs Test Result Data
Copyright (c) 2022 Cannlytics

Author: Keegan Skeate <https://github.com/keeganskeate>
Created: 7/8/2022
Updated: 7/8/2022
License: MIT License <https://github.com/cannlytics/cannlytics-ai/blob/main/LICENSE>

Description:

    Periodically collect recent lab results from
    SC Labs publicly published lab results.

Data Sources:
    
    - SC Labs Test Results
    URL: <https://client.sclabs.com/>

"""
# Internal imports.
from datetime import datetime
from hashlib import sha256
import hmac

# External imports.
from bs4 import BeautifulSoup
from cannlytics.utils import snake_case
import pandas as pd
import requests

# Constants.
BASE = 'https://client.sclabs.com'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'}
STATE = 'CA'

# Pertinent sample details (original key to final key).
DETAILS = {
    'batch_number': 'batch_number',
    'batch_size': 'batch_size',
    'business_name': 'distributor',
    'license_number': 'distributor_license_number',
    'sum_of_cannabinoids': 'sum_of_cannabinoids',
    'total_cannabinoids': 'total_cannabinoids',
    'total_thc': 'total_thc',
    'total_cbd': 'total_cbd',
    'total_cbg': 'total_cbg',
    'total_thcv': 'total_thcv',
    'total_cbc': 'total_cbc',
    'total_cbdv': 'total_cbdv',
    'total_terpenoids': 'total_terpenes',
    '9_thc_per_unit': 'cannabinoids_status',
    'pesticides': 'pesticides_status',
    'mycotoxins': 'mycotoxins_status',
    'residual_solvents': 'residual_solvents_status',
    'heavy_metals': 'heavy_metals_status',
    'microbiology': 'microbiology_status',
    'foreign_material': 'foreign_material_status',
}


def create_sample_id(private_key, public_key, salt='') -> str:
    """Create a hash to be used as a sample ID.
    The standard is to use:
        1. `private_key = producer`
        2. `public_key = product_name`
        3. `salt = date_tested`
    Args:
        private_key (str): A string to be used as the private key.
        public_key (str): A string to be used as the public key.
        salt (str): A string to be used as the salt, '' by default (optional).
    Returns:
        (str): A sample ID hash.
    """
    secret = bytes(private_key, 'UTF-8')
    message = snake_case(public_key) + snake_case(salt)
    sample_id = hmac.new(secret, message.encode(), sha256).hexdigest()
    return sample_id


def parse_data_block(div, tag='span') -> dict:
    """Parse an HTML data block into a dictionary.
    Args:
        div (bs4.element): An HTML element.
        tag (string): The type of tag that is repeated in the block.
    Returns:
        (dict): A dictionary of key and value pairs.
    """
    data = {}
    for el in div:
        try:
            label = el.find(tag).text
            value = el.text
            value = value.replace(label, '')
            value = value.replace('\n', '').strip()
            label = label.replace(':', '')
            data[snake_case(label)] = value
        except AttributeError:
            pass
    return data


#-----------------------------------------------------------------------
# Automate collection
#-----------------------------------------------------------------------

def get_sc_labs_test_results(client, reverse=True, limit=100, page_limit=100) -> list:
    """Get all test results for a specific SC Labs client.
    Args:
        client (str): A client number.
        reverse (bool): Whether to collect in reverse order, True by default (optional).
        limit (int): The number of samples per page to collect, 100 by default.
        page_limit (int): The maximum number of pages to collect, 100 by default.
    Returns:
        (list): A list of dictionaries of sample data.
    """

    #  Iterate over pages, getting all the samples on each page,
    # until the active page is repeated and the first sample is the same.
    active_page = None
    first_sample = None
    samples = []
    pages = range(1, page_limit)
    for page in pages:

        # Get a client page with X amount of samples.
        url = '/'.join([BASE, 'client', client])
        params = {'limit': limit, 'page': page}
        response = requests.get(url, headers=HEADERS, params=params)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Break the iteration if the page max is reached.
        current_sample = soup.find('h3').text
        current_page = soup.find('li', attrs={'class': 'pagination-active'})
        if (current_page == active_page) and (current_sample == first_sample):
            print('Repeat on page %i, collection finished: %s' % (page, client))
            break
        active_page = current_page
        first_sample = current_sample
        print('Collecting samples on page:', page)

        # Get producer.
        details = soup.find('div', attrs={'id': 'detailQuickView'})
        producer = details.find('h2').text

        # Get producer image.
        producer_image_url = details.find('img')['src'].replace('\n', '').strip()

        # Get producer website.
        element = details.find('span', attrs={'class': 'pp-social-web'})
        producer_url = element.find('a')['href']

        # Get all of the sample cards.
        cards = soup.find_all('div', attrs={'class': 'grid-item'})
        if reverse:
                cards.reverse()
        for card in cards:

            # Get the lab's internal ID.
            lab_id = card['id'].replace('div_', '')

            # Get the product name.
            product_name = card.find('h3').text

            # Get lab results URL.
            lab_results_url = BASE + card.find('a')['href']

            # Get the date tested.
            mm, dd, yyyy = card.find('h6').text.split('-')
            date = '-'.join([yyyy, mm, dd])

            # Get totals.
            totals = card.find('div', attrs={'class': 'sample-details'})
            values = totals.find_all('div')
            total_thc = values[0].text.split(':')[-1].replace('%', '')
            total_cbd = values[1].text.split(':')[-1].replace('%', '')
            total_terpenes = values[2].text.split(':')[-1].replace('%', '')

            # Create a sample ID.
            sample_id = create_sample_id(producer, product_name, date)

            # Aggregate sample data.
            sample = {
                'date_received': date,
                'lab_id': lab_id,
                'lab_results_url': lab_results_url,
                'producer': producer,
                'producer_image_url': producer_image_url,
                'product_name': product_name,
                'producer_url': producer_url,
                'sample_id': sample_id,
                'total_cbd': total_cbd,
                'total_thc': total_thc,
                'total_terpenes': total_terpenes,
            }
            samples.append(sample)
    
    # Return all of the samples for the client.
    return samples


def get_sc_labs_sample_details(sample) -> dict:
    """Get the details for a specific SC Labs test sample.
    Args:
        sample (str): A sample number.
    Returns:
        (dict): A dictionary of sample details.
    """

    # Get the sample page.
    url = '/'.join([BASE, 'sample', sample])
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get the bulk of the details.
    elements = soup.find_all('p', attrs={'class': 'sdp-summary-data'})
    details = parse_data_block(elements)

    # Get the producer details.
    element = soup.find('div', attrs={'id': 'cultivator-details'})
    producer_details = parse_data_block(element)

    # Format the distributor address.
    address = details['address'].split('*')[-1].strip()
    details['distributor_address'] = address
    details['distributor_city'] = address.split(',')[0]
    details['distributor_zip_code'] = address.split(' ')[-1]

    # Format the producer address.
    address = producer_details['address'].split('*')[-1].strip()
    details['address'] = address
    details['city'] = address.split(',')[0]
    details['zip_code'] = address.split(' ')[-1]

    # Get the Metrc IDs.
    metrc_ids = details['source_metrc_uid'].split(',')
    details['metrc_ids'] = [x.strip() for x in metrc_ids]

    # Get the product type.
    details['product_type'] = soup.find('p', attrs={'class': 'sdp-producttype'}).text

    # Get the image.
    image_url = soup.find('a', attrs={'data-popup': 'fancybox'})['href']
    details['images'] = [{'url': image_url, 'filename': image_url.split('/')[-1]}]

    # Get the date tested.
    element = soup.find('div', attrs={'class': 'sdp-masthead-data'})
    mm, dd, yyyy = element.find('p').text.split('/')
    details['date_tested'] = '-'.join([yyyy, mm, dd])

    # Get the overall status: Pass / Fail.
    status = soup.find('p', attrs={'class': 'sdp-result-pass'}).text
    details['status'] = status.replace('\n', '').strip()

    # Format the dates.
    mm, dd, yyyy = details['date_collected'].split('/')
    details['date_collected'] = '-'.join([yyyy, mm, dd])
    mm, dd, yyyy = details['date_received'].split('/')
    details['date_received'] = '-'.join([yyyy, mm, dd])
    
    # Rename desired fields.
    for key, value in DETAILS.items():
        details[value] = details.pop(key)

    # Get the CoA ID.
    details['coa_id'] = soup.find('p', attrs={'class': 'coa-id'}).text.split(':')[-1]

    # Optional: Try to get sample_weight.

    # Get all of the analyses and results.
    analyses = []
    results = []
    notes = None
    cards = soup.find_all('div', attrs={'class': 'analysis-container'})
    for element in cards:

        # Get the analysis.
        analysis = element.find('h4').text
        if 'Notes' in analysis:
            div = element.find('div', attrs={'class': 'section-inner'})
            notes = div.find('p').text
        if 'Analysis' not in analysis:
            continue
        analysis = snake_case(analysis.split(' Analysis')[0])
        analyses.append(analysis)

        # Get the method for the analysis.
        bold = element.find('b')
        method = bold.parent.text.replace('Method: ', '')
        key = '_'.join([analysis, 'method'])
        details[key] = method

        # Get all of the results for the analysis.
        # - value, units, margin_of_error, lod, loq
        table = element.find('table')
        rows = table.find_all('tr')
        for row in rows[1:]:
            cells = row.find_all('td')
            result = {}
            for cell in cells:
                key = cell['class'][0].replace('table-', '')
                value = cell.text.replace('\n', '').strip()
                result[key] = value
                result['analysis'] = analysis
            results.append(result)

    # Aggregate the sample details.
    data = {'notes': notes, 'results': results}
    return {**data, **details}


#-----------------------------------------------------------------------
# Test the functionality.
#-----------------------------------------------------------------------

# Get all test results for a specific client.
# test_results = get_sc_labs_test_results('2821')

# Get details for a specific sample.
sample_details = get_sc_labs_sample_details('858084')


#-----------------------------------------------------------------------
# Test full scrape.
#-----------------------------------------------------------------------
# 1. Discover all SC Labs public clients by scanning:
#
#       https://client.sclabs.com/client/{client}/
#
# 2. Iterate over pages for each client, collecting samples until
# the 1st sample and active page are the same:
# 
#       https://client.sclabs.com/client/{client}/?page={page}
#
# 3. (a) Get the sample details for each sample found.
#    (b) Save the sample details.
#-----------------------------------------------------------------------

# # 1. and 2. Iterate over potential client pages and client sample pages.
# start = datetime.now()
# errors = []
# test_results = []
# PAGES = range(1_000, 10_000)
# pages = list(PAGES)
# pages.reverse()
# for page in pages:
#     try:
#         results = get_sc_labs_test_results(str(page))
#         test_results += results
#         print('Collected sample results on page:', page)
#     except:
#         errors.append(page)

# # 3a. Get the sample details for each sample found.
# total = len(test_results)
# for i, test_result in enumerate(test_results):
#     sample = test_result['lab_results_url'].split('/')[-1]
#     print('Collecting (%i/%i):' % (i + 1, total), sample)
#     details = get_sc_labs_sample_details(sample)
#     test_results[i] = {**test_result, **details}

# # 3b. Save the results.
# data = pd.DataFrame(test_results)
# timestamp = datetime.now().isoformat()[:19].replace(':', '-')
# datafile = f'../../.datasets/lab-results/sc-lab-results-{timestamp}.xlsx'
# data.to_excel(datafile, index=False)
# end = datetime.now()
# print('Runtime took:', end - start)


#-----------------------------------------------------------------------
# Test scrape most recent.
#-----------------------------------------------------------------------
# 1. Discover all SC Labs public clients.
# 2. Get the most recent 100 samples for each client.
# 3. (a) Get the sample details for each sample found.
#    (b) Save the sample details.
#-----------------------------------------------------------------------

# 1. Discover all SC Labs public clients.


# 2. Get the most recent 100 samples for each client.


# 3a. Get the details for the most recent samples.


# 3b. Save the most recent samples.



#-----------------------------------------------------------------------
# Future work: Processing the raw data.
#-----------------------------------------------------------------------

# TODO: Augment lab data:
# - lab_id
# - lab_name


# TODO: Augment the `state`.


# TODO: Find the `county` for the `zip_code`.


# TODO: Normalize the `results`, `images`.


# TODO: Standardize the `product_type` and `status`.

# Separate `lod` and `loq`.

# Rename `mu` to `margin_of_error`.
# Remove: ±

# Separate `batch_units` from `batch_size`.

# Handle values and units.
# result-mass -> mg_g
# result-percent -> value
# units = 'percent'


# Rename `compound` to `name` and add `key`.
# Rename `action-limit` to `limit`
# `result-mass` to `value`
# `result-pf` to `status`

# Handle:
# - total_terpenoids_mgtog, total_terpenoids_percent

# TODO: Standardize the analyte names!
