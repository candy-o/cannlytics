"""
Test Statistics API Endpoint | Cannlytics API

Authors: Keegan Skeate <https://github.com/keeganskeate>
Created: 5/26/2021
Updated: 6/1/2021
License: MIT License <https://opensource.org/licenses/MIT>
"""
# Standard imports.
import os
import requests

# External imports.
from dotenv import load_dotenv
import pandas as pd


# Specify the API server base URL.
BASE = 'http://127.0.0.1:8000/api'
# BASE = 'https://console.cannlytics.com/api' # Uncomment for production.


# TODO: Implement API key.
# # Pass your API key through the authorization header as a bearer token.
# load_dotenv('../../../.env')
# API_KEY = os.getenv('CANNLYTICS_API_KEY')
# HEADERS = {
#     'Authorization': 'Bearer %s' % API_KEY,
#     'Content-type': 'application/json',
# }

#-----------------------------------------------------------------------
# Get model statistics..
#-----------------------------------------------------------------------

# Get statistics for the `full` model.
url = f'{BASE}/stats/effects'
params = {'model': 'full'}
response = requests.get(url, params=params)
assert response.status_code == 200
model_stats = response.json()['data']
print(model_stats)


#-----------------------------------------------------------------------
# Post lab results to get potential effects and aromas.
#-----------------------------------------------------------------------

# Post lab results to get potential effects and aromas.
data = {
    'model': 'simple', # full
    'samples': [
        {'total_cbd': 1.0, 'total_thc': 18.0},
        {'total_cbd': 1.0, 'total_thc': 20.0},
        {'total_cbd': 1.0, 'total_thc': 30.0},
        {'total_cbd': 7.0, 'total_thc': 7.0},
    ]
}
url = f'{BASE}/stats/effects'
response = requests.post(url, json=data)
assert response.status_code == 200
data = response.json()['data']
model_stats = data['model_stats']
samples = pd.DataFrame(data['samples'])

# Collect outcomes.
outcomes = pd.DataFrame()
for index, row in samples.iterrows():
    print(f'\nSample {index}')
    print('-------------')
    for i, key in enumerate(row['potential_effects']):
        tpr = round(model_stats['true_positive_rate'][key] * 100, 2)
        fpr = round(model_stats['false_positive_rate'][key] * 100, 2)
        title = key.replace('effect_', '').replace('_', ' ').title()
        print(title, f'(TPR: {tpr}%, FPR: {fpr}%)')
        outcomes = pd.concat([outcomes, pd.DataFrame([{
            'tpr': tpr,
            'fpr': fpr,
            'name': title,
            'strain_name': index,
        }])])


#-----------------------------------------------------------------------
# Post actual aromas and effects for the strains.
#-----------------------------------------------------------------------

# Post actual aromas and effects, rating the usefulness of the prediction.
data = {
    'samples': [
        {
            'prediction_id': '01g4g8apexj1r426rbkcnfdjt9',
            'strain_name': 'Test Strain',
            'effects': ['happy', 'focused'],
            'aromas': ['citrus', 'pine'],
            'rating': 10,
        },
    ]
}
url = f'{BASE}/stats/effects/actual'
response = requests.post(url, json=data)
assert response.status_code == 200
message = response.json()['message']
print(message)
