#allows for us to make API calls
import requests

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

