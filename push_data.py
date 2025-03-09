import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract:
    def __init__(self):
        try:
            pass  # No need for try-except here
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            records = data.to_dict(orient="records")  # More efficient
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            db = mongo_client[database]
            coll = db[collection]
            coll.insert_many(records)
            return len(records)  # Return number of inserted records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

        
if __name__=='__main__':
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="NOUMANAI"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)


