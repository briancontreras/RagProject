#imports LegiScanAPI class previously defined
from LegiScanAPI import LegiScanAPI
import zipProcessor
import os


api = LegiScanAPI(  )

jsonFile = api.get_dataset_list("CA", 2024)
print(jsonFile)
id = jsonFile[0]['session_id']
access_key = jsonFile[0]['access_key']
print(id)
print(access_key)

jsonFile = zipProcessor.parse_zip_response(api.get_dataset(id,access_key,"json"))
print(jsonFile)



