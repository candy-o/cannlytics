"""
Data Tools | Cannlytics
Copyright (c) 2022 Cannlytics

Authors: Keegan Skeate <https://github.com/keeganskeate>
Created: 4/21/2022
Updated: 7/12/2022
License: <https://github.com/cannlytics/cannlytics/blob/main/LICENSE>
"""
# Internal imports.
from optparse import OptionError
import os
from typing import Any, List, Optional

# External imports.
from fredapi import Fred
import pandas as pd

# Internal imports.
from cannlytics.utils import rmerge


DATA_URL = 'https://cannlytics.com/api/data'


#-----------------------------------------------------------------------
# Data collection tools.
#-----------------------------------------------------------------------

# TODO:
def download_dataset():
    """Download a specific dataset."""

    raise NotImplementedError


# TODO:
def get_data_catalogue():
    """Get the Cannlytics data catalogue."""

    raise NotImplementedError


# FIXME: Can these 2 functions be combined?
def get_state_population(
        api_key: str,
        state: str,
        district: Optional[str] = '',
        obs_start: Optional[Any] = None,
        obs_end: Optional[Any] = None,
        multiplier: Optional[float] = 1000.0,
    ) -> List[int]:
    """Get a given state's population from the Fed Fred API."""
    fred = Fred(api_key=api_key)
    population = fred.get_series(f'{state}POP{district}', obs_start, obs_end)
    try:
        population = [int(x * multiplier) for x in population.values]
        if len(population) == 1:
            return population[0]
    except ValueError:
        pass
    return population


def get_state_current_population(state: str, api_key: Optional[str] = None) -> dict:
    """Get a given state's latest population from the Fed Fred API,
    getting the number in 1000's and returning the absolute value.
    Args:
        state (str): The state abbreviation for the state to retrieve population
            data. The abbreviation can be upper or lower case.
        api_key (str): A Fed FRED API key. You can sign up for a free API key at
            http://research.stlouisfed.org/fred2/. You can also pass `None`
            and set the environment variable 'FRED_API_KEY' to the value of
            your API key.
    Returns:
        (dict): Returns a dictionary with population values and source.
    """
    fred = Fred(api_key=api_key)
    state_code = state.upper()
    population_source_code = f'{state_code}POP'
    population = fred.get_series(population_source_code)
    real_population = int(population.iloc[-1] * 1000)
    population_date = population.index[-1].isoformat()[:10]
    return {
        'population': real_population,
        'population_formatted': f'{real_population:,}',
        'population_source_code': population_source_code,
        'population_source': f'https://fred.stlouisfed.org/series/{population_source_code}',
        'population_at': population_date,
    }


#-----------------------------------------------------------------------
# Data aggregation tools.
#-----------------------------------------------------------------------

def aggregate_datasets(
        directory: str,
        on: Optional[str] = 'sample_id',
        how: Optional[str] = 'left',
        replace: Optional[str] = 'right',
        reverse: Optional[bool] = True,
        concat=False
    ) -> pd.DataFrame:
    """Aggregate datasets. Leverages `rmerge` to combine
    each dataset in the given directory.
    Args:
        directory (string): Required dataset directory.
        on (string): The key to merge datasets, `sample_id` by default (optional).
        how (string): How to merge, `left` by default (optional).
        replace (string): How to replace, `right` by default (optional).
        reverse (bool): Whether to combine in reverse order, `True` by default (optional).
    Returns:
        (DataFrame): The aggregated data.
    """
    all_data = None
    files = os.listdir(directory)
    if reverse:
        files.reverse()
    for filename in files:
        datafile = os.path.join(directory, filename)
        try:
            data = pd.read_excel(datafile)
        except:
            continue
        if all_data is None:
            all_data = data
        else:
            if concat:
                all_data = pd.concat([all_data, data])
            else:
                all_data = rmerge(
                    all_data,
                    data,
                    on=on,
                    how=how,
                    replace=replace,
                )
    return all_data


# TODO:
def shard_datasets(data, directory, count=10_000):
    """Shard a dataset for ease of use."""

    raise NotImplementedError


#-----------------------------------------------------------------------
# Data cleaning tools.
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------
# Data augmentation tools.
#-----------------------------------------------------------------------



if __name__ == '__main__':

    print('Performing tests...')

    # TODO: Test each function here!

    # Test `aggregate_datasets`.
    data_dir = '../../.datasets/lab_results/raw_data/psi_labs'
    data = aggregate_datasets(data_dir)
    subset = data.loc[~data['results'].isnull()]
    subset.drop_duplicates(subset='sample_id', keep='first', inplace=True)
    subset.to_excel('../../.datasets/lab_results/psi_labs_test_results.xlsx')

    # Test `aggregate_datasets`.
    data_dir = '../../.datasets/lab_results/raw_data/sc_labs'
    data = aggregate_datasets(data_dir)
    subset = data.loc[~data['results'].isnull()]
    subset.drop_duplicates(subset='sample_id', keep='first', inplace=True)
    subset.to_excel('../../.datasets/lab_results/sc_labs_test_results.xlsx')
