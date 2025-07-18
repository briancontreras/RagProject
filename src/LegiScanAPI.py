#allows for us to make API calls
import requests
#Needs Json class to utilize json response data
import json

#imports for zip file
import zipfile
import base64
import io
from pathlib import Path
import logging


#classes to load env api key
import os
from dotenv import load_dotenv

from typing import Optional,Dict,List, Any 
from zipProcessor import process_zip,read_zip

class LegiScanAPI:
    #function to initialize Api key and create API session
    def __init__(self, api_key: Optional[str] = None):
        load_dotenv()
        self.api_key = api_key or os.getenv('LegiScan_Key')
        if not self.api_key:
            raise ValueError("The LegiScan API key can't be found")
        
        #sets base url
        self.base_url = "https://api.legiscan.com"

        #sets session to not have to make multiple requests
        self.session = requests.Session()
    def _make_request(self, endpoint: str, params: Dict = None) -> Dict:
        if params is None:
            params = {}
        params['key'] = self.api_key

        try:
            print(f"{self.base_url}{endpoint}")
            response = self.session.get(f"{self.base_url}{endpoint}", params=params)
            response.raise_for_status()

            data = response.json()
            
            if data.get('status') == 'ERROR':
                raise Exception(f"API ERROR: {data.get('alert', 'Unknown error')}")

            return data
        except requests.exceptions.RequestException as e:
            print(f"Request failed {e}")
            raise
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON response: {e}")
            raise
    
    def get_dataset_list(self, state: Optional[str] = None, year: Optional[int] = None) -> List[Dict]:
        # LegiScan API uses 'op' parameter for operations
        params = {'op': 'getDatasetList'}

        if state:  
            params['state'] = state
        if year:
            params['year'] = year
        
        # Use root path with query parameters instead of /datasetlist
        response = self._make_request('/', params)
        return response.get('datasetlist', [])
    
    def get_dataset(self, id: Optional[str] = None, accessKey: Optional[int] = None, format: Optional[str] = None):
        params = {'op' : 'getDataset'}

        if id:
            params['id'] = id
        if accessKey:
            params['access_key'] = accessKey
        if format:
            params['format'] = format
        
        response = self._make_request('/',params)
        dataset = response.get('dataset',[])

        if process_zip and isinstance(dataset, dict) and 'zip' in dataset:
            dataset['zip_file'] = read_zip(dataset['zip'])

        
        return dataset
    

