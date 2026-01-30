from pymongo import MongoClient
import os


#local database
db_client = MongoClient().local

#Remote database
# MONGO_URI = os.getenv("MONGO_URI")
# db_client = MongoClient(MONGO_URI).test