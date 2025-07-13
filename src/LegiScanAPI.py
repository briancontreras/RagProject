#allows for us to make API calls
import requests
#Needs Json class to utilize json response data
import json

#classes to load env api key
import os
from dotenv import load_dotenv


class LegiScanAPI:
    #function to initialize Api key and create API session
    def __init__(self, api_key: Optional[str] = None):

        #checks if the API key exists in the .env file
        self.api_key = os.getenv('LegiScan_Key')
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
            response = self.session.get(f"{self.base_url}{endpoint}", params=params)
            response.raise_for_status

            data = response.json
            
            if data.get('status') == 'ERROR':
                raise Exception(f"API ERROR: {data.get('alert', 'Unknown error')}")

            return data
        except requests.exceptions.RequestException as e:
            print(f"Request failed {e}")
            raise
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON response: {e}")
            raise

