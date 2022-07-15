"""
Get MCR Labs Test Result Data
Copyright (c) 2022 Cannlytics

Author: Keegan Skeate <https://github.com/keeganskeate>
Created: 7/13/2022
Updated: 7/14/2022
License: MIT License <https://github.com/cannlytics/cannlytics/blob/main/LICENSE>

Description:

    Periodically collect recent lab results from
    MCR Labs publicly published lab results.

    Data points collected for each sample include:

        ✓ analyses
        ✓ product_name
        ✓ product_type
        ✓ producer
        ✓ date_tested
        ✓ total_cannabinoids
        ✓ total_terpenes
        ✓ lab_results_url
        ✓ image
        ✓ sample_id (generated)
        ✓ results
        ✓ lab
        ✓ {analysis}_method

Data Sources:
    
    - MCR Labs Test Results
    URL: <https://reports.mcrlabs.com>

Future development:

    - Implement the function to get all of a given client's lab results.
    - Optional: Create necessary data dirs automatically.
    - Optional: Function to download any pre-existing results.

"""
# Internal imports.
from datetime import datetime
import json
import math
from time import sleep
from typing import Any, Optional

# External imports.
from bs4 import BeautifulSoup
import pandas as pd
import requests

# Internal imports.
from cannlytics.data.data import create_sample_id
from cannlytics.utils.utils import (
    snake_case,
    to_excel_with_style,
)


# === Constants ===
BASE = 'https://reports.mcrlabs.com'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'}
STATE = 'MA'
DATA_DIR = '../../../.datasets/lab_results'
RAW_DATA = '../../../.datasets/lab_results/raw_data/mcr_labs'
TRAINING_DATA = '../../../.datasets/lab_results/training_data'


def format_iso_date(date, sep='/'):
    """Format a human-written date into an ISO formatted date."""
    mm, dd, yyyy = tuple(date.split(sep))
    if len(mm) == 1:
        mm = f'0{mm}'
    if len(dd) == 1:
        dd = f'0{dd}'
    if len(yyyy) == 2:
        yyyy = f'20{yyyy}'
    return '-'.join([yyyy, mm, dd])


def strip_whitespace(string):
    """Strip whitespace from a string."""
    return string.replace('\n', '').strip()


def get_mcr_labs_sample_count(per_page: Optional[int] = 30) -> dict:
    """Get the number of samples and pages of MCR Labs samples."""
    url = f'{BASE}/products-weve-tested'
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    element = soup.find('span', attrs={'id': 'found_posts'})
    count = int(element.text.replace(',', ''))
    pages = math.ceil(count / per_page)
    return {'count': count, 'pages': pages}


def get_mcr_labs_test_results(
        starting_page: Optional[int] = 1,
        ending_page: Optional[int] = None,
        pause: Optional[float] = 3,
        verbose: Optional[bool] = True
    ) -> list:
    """Get all MCR Labs test results.
    Args:
        starting_page (int): The page to start collecting results,
            `1` by default (optional).
        ending_page (int): The page to end collecting results,
            `None` by default, which will collect to the end (optional).
        pause (float): The amount of time to wait between requests.
        verbose (bool): Whether to print out status, `True` by default
            (optional).
    Returns:
        (list): The complete sample data.
    """
    # Iterate over all of the pages.
    page_count = get_mcr_labs_sample_count()
    total_pages = page_count['pages']
    if not ending_page:
        ending_page = total_pages + 1
    if verbose:
        print('Getting samples for pages %i to %i.' % (starting_page, ending_page))
    samples = []
    for page_id in range(starting_page, ending_page):
        sample_data = get_mcr_labs_samples(page_id)
        samples += sample_data
        if page_id > 1 and page_id < ending_page:
            sleep(pause)
    if verbose:
        print('Found %i samples.' % len(samples))

    # Get all of the sample details.
    rows = []
    for i, sample in enumerate(samples):
        sample_id = sample['lab_results_url'].split('/')[-1]
        details = get_mcr_labs_sample_details(sample_id)
        rows.append({**sample, **details})
        if i > 1:
            sleep(pause)
        if verbose:
            print('Collected sample:', sample_id)
    
    # Optional: Clean the data after collection?
    # - Map product types.
    # - Parse units from results
    # data = pd.DataFrame(rows)
    
    # Return all of the sample data.
    return rows


def get_mcr_labs_samples(
        page_id: Any,
        cat: Optional[str] = 'all',
        order: Optional[str] = 'date-desc',
        search: Optional[str] = '',
    ) -> list:
    """Get all test results from MCR Labs on a specific page.
    Args:
        page_id (str|int): The page number to get samples.
        cat (str): The category, `all` by default (optional). Options:
            `flower`, `concentrate`, `extract`, `mip`.
        order (str): The order to list results, `date-desc` by default
            (optional). Options: `date-desc`, `samplename`, `client`,
            `totalcann-desc`, `totalterp-desc`, `maxthc-desc`, `maxcbd-desc`.
        search (str): A particular search query.
    Returns:
        (list): A list of dictionaries of sample data.
    """
    # Get a page.
    url = f'{BASE}/ProductWeVeTested/AjaxSearch'
    params = {
        'category': cat,
        'order': order,
        'page': str(page_id),
        'searchString': search,
    }
    response = requests.get(url, headers=HEADERS, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get all of the products on the page.
    samples = []
    products = soup.find_all('li', attrs={'class': 'grid-item'})
    for product in products:

        # Get sample details.
        sample = {}
        details = product.find('div', attrs={'class': 'reportTable'})
        sample['product_name'] = details.find('div', \
            attrs={'class': 'fth_name'}).text
        sample['producer'] = details.find('div', \
            attrs={'class': 'fth_client'}).text
        sample['product_type'] = details.find('div', \
            attrs={'class': 'fth_category'}).text
        sample['total_cannabinoids'] = strip_whitespace(details.find('div', \
            attrs={'class': 'fth_cannabinoids'}).text)
        sample['total_terpenes'] = strip_whitespace(details.find('div', \
            attrs={'class': 'fth_terpenes'}).text)
        try:
            sample['date_tested'] = format_iso_date(details.find('div', \
                attrs={'class': 'fth_date'}).text)
        except ValueError:
            print('Error:', sample)
            sample['date_tested'] = ''

        # Try to get the producer's URL.
        try:
            element = product.find('span', attrs={'class': 'url-linked'})
            href = element.attrs['data-url']
            sample['producer_url'] = '/'.join([BASE, href])
        except AttributeError:
            sample['producer_url'] = ''

        # Get the lab results URL.
        href = product.find('a')['href']
        sample['lab_results_url'] = '/'.join([BASE, href])

        # Get the image.
        image_url = product.find('img')['src']
        filename = image_url.split('/')[-1]
        sample['images'] = [{'url': image_url, 'filename': filename}]

        # Create a sample ID.
        sample['sample_id'] = create_sample_id(
            private_key=sample['producer'],
            public_key=sample['product_name'],
            salt=sample['date_tested'],
        )

        # Aggregate sample data.
        samples.append(sample)

    # Return the samples.
    return samples


def get_mcr_labs_producer_test_results():
    """Get all test results from MCR Labs for a specific producer.
    Returns:
        (list): A list of dictionaries of sample data.
    """
    # TODO: Implement.
    raise NotImplementedError


def get_mcr_labs_sample_details(sample_id: str) -> dict:
    """Get the details for a specific MCR Labs test sample.
    Args:
        sample_id (str): A sample ID number.
    Returns:
        (dict): A dictionary of sample details.
    """
    # Get the sample page.
    sample = {}
    url = f'{BASE}/reports/{sample_id}'
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Optional: Get product serving size.

    # Get the lab.
    element = soup.find('div', attrs={'class': 'rd_date'})
    sample['lab'] = strip_whitespace(element.text).split('by ')[-1]

    # Get sample test results.
    analyses = []
    results = []

    # Get the methods.
    details = soup.find_all('div', attrs={'class': 'calc-expl'})
    for detail in details:
        pars = detail.find_all('p')
        for par in pars:
            if 'quantified' in par.text:
                text = strip_whitespace(par.text)
                analysis = snake_case(text.split(' are quantified')[0])
                method = text.split('quantified using ')[-1]\
                        .replace('.', '').title()
                sample[f'{analysis}_method'] = method
                analyses.append(analysis)

    # Get the cannabinoids.
    scripts = soup.find_all('script')
    for script in scripts:
        if script.string:
            if 'dataProvided' in script.string:
                break
    block = script.string.split('const dataProvided = ')[-1].split(';')[0]
    block = strip_whitespace(block).replace(' ', '').replace(',]', ']')
    cannabinoids = json.loads(block)
    analyses.append('cannabinoids')
    for analyte in cannabinoids:
        results.append({
            'key': analyte['key'],
            'name': analyte['label'],
            'value': analyte['perc'],
            'units': 'percent',
        })

    # Get the results for all other analyses.
    values = ['name', 'result', 'lod' ,'loq']
    tables = soup.find_all('table', attrs={'class': 'safetytable'})
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            result = {}
            cells = row.find_all('td')
            if len(cells) > 1:
                for i, cell in enumerate(cells):
                    try:
                        key = values[i]
                    except IndexError:
                        key = f'limit_{i}'
                    result[key] = cell.text
                if result:
                    results.append(result)

    # Return the sample details.
    sample['results'] = results
    return sample


# === 3. Archive the data! ===


if __name__ == '__main__':

    # === Test ===

    # ✓ Test getting the number of total samples.
    # page_count = get_mcr_labs_sample_count(per_page=30)

    # ✓ Test getting samples on a given page.
    # samples = get_mcr_labs_samples('6')

    # ✓ Test getting sample details.
    # details = get_mcr_labs_sample_details('rooted-labs-distillate_2')

    # ✓ Get all of the samples.
    print('Getting ALL of the samples.')
    all_results = get_mcr_labs_test_results(
        starting_page=5,
        ending_page=25,
        pause=0.2,
    )
    timestamp = datetime.now().isoformat()[:19].replace(':', '-')
    datafile = f'{DATA_DIR}/mcr-lab-results-{timestamp}.xlsx'
    to_excel_with_style(pd.DataFrame(all_results), datafile)
    print('[✓] Tested getting ALL of the samples.')

    # ✓ Get only the most recent samples.
    # print('Getting the most recent samples.')
    # recent_results = get_mcr_labs_test_results(ending_page=2)
    # timestamp = datetime.now().isoformat()[:19].replace(':', '-')
    # datafile = f'{DATA_DIR}/mcr-lab-results-{timestamp}.xlsx'
    # to_excel_with_style(pd.DataFrame(recent_results), datafile)
    # print('[✓] Tested getting the most recent samples.')