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

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self, records, database, collection):
        try:
                self.database = database
                self.collection = collection
                self.records = records
        
                # Alternative connection approach
                host = "cluster0.epl8o.mongodb.net"
                user = "pranaynepalia015"
                password = "Admin123"
                
                uri = f"mongodb+srv://{user}:{password}@{host}/?retryWrites=true&w=majority"
                
                self.mongo_client = pymongo.MongoClient(uri, tlsCAFile=certifi.where())
                self.database = self.mongo_client[self.database]
                self.collection = self.database[self.collection]
                self.collection.insert_many(self.records)
                return(len(self.records))
        except Exception as e:
            print(f"Connection error details: {type(e).__name__}: {str(e)}")
            raise NetworkSecurityException(e, sys)
        
if __name__=='__main__':
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="PRANAYAI"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)
        