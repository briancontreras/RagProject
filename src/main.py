#imports LegiScanAPI class previously defined
from LegiScanAPI import LegiScanAPI
import zipProcessor
import os
import base64



api = LegiScanAPI(  )

jsonFile = api.get_dataset_list("CA", 2024)
print(jsonFile)
id = jsonFile[0]['session_id']
access_key = jsonFile[0]['access_key']
print(id)
print(access_key)
dataset = api.get_dataset(id,access_key,"json")
dataset = base64.decode(dataset)

with open("zipCache", 'a',encoding="utf-8") as file:
            file.write(dataset)

# zip_file = zipProcessor.extract_all_from_base64_zip(dataset , "./extracted_data")




