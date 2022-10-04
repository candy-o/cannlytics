"""
Geographic Information Systems (GIS) Data | Cannlytics
Copyright (c) 2021-2022 Cannlytics and Cannlytics Contributors

Authors: Keegan Skeate <https://github.com/keeganskeate>
Created: 11/5/2021
Updated: 7/31/2022
License: <https://github.com/cannlytics/cannlytics/blob/main/LICENSE>

Description:

    This script contains useful GIS functions.

"""
# Standard imports.
from time import sleep
from typing import Any, List, Optional

# External imports.
from fredapi import Fred
from googlemaps import Client, places
import zipcodes

# Internal imports.
from cannlytics.firebase import initialize_firebase, get_document


def get_google_maps_api_key() -> str:
    """Get Google Maps API key.
    Returns:
        (str): Returns the Google Maps API key stored
            in the Firestore database.
    """
    # TODO: Prefer using secret manager to Firestore for secrets.
    database = initialize_firebase()
    data = get_document('admin/google', database=database)
    return data['google_maps_api_key']


def get_state_data(
        state: str,
        code: str,
        fred_api_key: Optional[str] = None,
        district: Optional[str] = '',
        obs_start: Optional[Any] = None,
        obs_end: Optional[Any] = None,
    ) -> dict:
    """Get a given state's data from the Fed Fred API, given a data code.
    Args:
        state (str): The state abbreviation for the state to retrieve data.
        code (str): The FRED code for the data, for example "POP".
        fred_api_key (str): A Fed FRED API key. You can sign up for a free API key at
            http://research.stlouisfed.org/fred2/. You can also pass `None`
            and set the environment variable 'FRED_API_KEY' to the value of
            your API key.
    Returns:
        (dict): Returns a dictionary with population values and source.
    """
    fred = Fred(api_key=fred_api_key)
    code = f'{state.upper()}{code.upper()}{district.upper()}'
    series = fred.get_series(code, obs_start, obs_end)
    if len(series) == 1:
        return series[0]
    return series


def get_state_population(
        state: str,
        fred_api_key: Optional[str] = None,
        district: Optional[str] = '',
        obs_start: Optional[Any] = None,
        obs_end: Optional[Any] = None,
        multiplier: Optional[float] = 1000.0,
    ) -> dict:
    """Get a given state's latest population from the Fed Fred API,
    getting the number in 1000's and returning the absolute value.
    Args:
        state (str): The state abbreviation for the state to retrieve
            population data. The abbreviation can be upper or lower case.
        fred_api_key (str): A Fed FRED API key. You can sign up for a free API key at
            http://research.stlouisfed.org/fred2/. You can also pass `None`
            and set the environment variable 'FRED_API_KEY' to the value of
            your API key.
    Returns:
        (dict): Returns a dictionary with population values and source.
    """
    pops = []
    fred = Fred(api_key=fred_api_key)
    code = f'{state.upper()}POP{district.upper()}'
    series = fred.get_series(code, obs_start, obs_end)
    for index, value in series.iteritems():
        real_pop = int(value * multiplier)
        pops.append({
            'population': real_pop,
            'population_formatted': f'{real_pop:,}',
            'population_source_code': code,
            'population_source': f'https://fred.stlouisfed.org/series/{code}',
            'population_at': index.isoformat()[:10],
        })
    if len(pops) == 1:
        return pops[0]
    return pops


def geocode_addresses(
        data,
        api_key: Optional[str] = None,
        pause: Optional[float] = 0.0,
        address_field: Optional[str] = '',
    ) -> Any:
    """Geocode addresses in a dataframe.
    Args:
        data (DataFrame): A DataFrame containing the addresses to geocode.
        api_key (str): A Google Maps API key.
        pause (float): An optional pause to wait between requests, 0.0 by default.
        address_field (str): An optional field to specify the address field,
            otherwise assumes the DataFrame has `street`, `city`, `state`,
            and `zip_code` columns.
    Returns:
        (DataFrame): Returns the DataFrame with `latitude`, `longitude`,
        and `formatted_address` columns.
    """
    if api_key is None:
        api_key = get_google_maps_api_key()
    gmaps = Client(key=api_key)
    for index, item in data.iterrows():
        if index and pause:
            sleep(pause)
        if address_field:
            address = item.address
        else:
            address = f'{item.street}, {item.city}, {item.state} {item.zip_code}'
        geocode_result = gmaps.geocode(address)
        if geocode_result:
            data.at[index, 'formatted_address'] = geocode_result[0]['formatted_address']
            location = geocode_result[0]['geometry']['location']
            data.at[index, 'latitude'] = location['lat']
            data.at[index, 'longitude'] = location['lng']
            for info in geocode_result[0]['address_components']:
                key = info['types'][0]
                if key == 'administrative_area_level_1':
                    data.at[index, 'state'] = info['short_name']
                    data.at[index, 'state_name'] = info['long_name']
                if key == 'administrative_area_level_2':
                    data.at[index, 'county'] = info['long_name']
    return data


def search_for_address(
        query: str,
        api_key: Optional[str] = None,
        fields: Optional[List[str]] = None,
    ) -> dict:
    """Search for the address of a given name.
    Args:
        query (str): The text to use to search for an address.
        api_key (): Optional, None by default.
        fields (list): Optional, `formatted_address` is included by default.
    Returns:
        (list): A list of potential results.
    Raises:
        (IndexError): Raises an `IndexError` if no candidate is found.
    """
    if api_key is None:
        api_key = get_google_maps_api_key()
    if fields is None:
        fields = [
            'formatted_address',
            'geometry/location/lat',
            'geometry/location/lng',
        ]
    gmaps = Client(key=api_key)
    search = places.find_place(gmaps, query, 'textquery')
    place_id = search['candidates'][0]['place_id']
    place = places.place(gmaps, place_id, fields=fields)
    result = place['result']
    candidate = {}
    if result.get('geometry'):
        location = result['geometry']['location']
        candidate['latitude'] = location['lat']
        candidate['longitude'] = location['lng']
        del result['geometry']
    if result.get('formatted_address'):
        formatted_address = result['formatted_address']
        parts = formatted_address.split(',')
        candidate['street'] = parts[0]
        candidate['city'] = parts[1].strip()
        candidate['state'], candidate['zipcode'] = tuple(parts[2].strip().split(' '))
        try:
            candidate['county'] = zipcodes.matching(candidate['zipcode'])[0]['county']
        except:
            candidate['county'] = ''
    return {**result, **candidate}
