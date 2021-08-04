"""
Upload State | Cannlytics Console

Author: Keegan Skeate
Contact: <keegan@cannlytics.com>
Created: 7/5/2021
Updated: 7/5/2021
License: MIT License <https://opensource.org/licenses/MIT>
"""

import os
import environ

import sys
sys.path.append('../../')
from cannlytics import firebase # pylint: disable=import-error
from console import state

if __name__ == '__main__':

    # Initialize Firebase.
    env = environ.Env()
    env.read_env('../../.env')
    credentials = env('GOOGLE_APPLICATION_CREDENTIALS')
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials
    db = firebase.initialize_firebase()
    
    # Upload state data to Firestore.
    for key, data_model in state.material['data_models'].items():
        firebase.update_document(f'public/state/data_models/{key}', data_model)
        firebase.update_document(f'organizations/test-company/data_models/{key}', data_model)

    # Upload traceability settings to Firestore.
    # traceability = state.material['traceability']
    # firebase.update_document('public/state/traceability/traceability_settings', traceability)
    # firebase.update_document('organizations/test-company/organization_settings/traceability_settings', traceability)