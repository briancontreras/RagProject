#imports LegiScanAPI class previously defined
from LegiScanAPI import LegiScanAPI
import os


api = LegiScanAPI(  )

jsonFile = api.get_dataset_list("CA", 2024)
print(jsonFile)
api.session.close()

# jsonFile = api.get_dataset_list()
# print(jsonFile)
