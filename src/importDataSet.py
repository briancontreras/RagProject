#allows for us to make API calls
import requests

#classes to load env api key
import os
from dotenv import load_dotenv

#import legiscan_api class
from legiscan_api import LegiScanAPI

#load API Key int work enviroment
load_dotenv() 
os.environ['LegiScan_Key'] = os.getenv('LegiScan_Key')


#Since we will only be importing data we will only use the GET request
response = requests.get()