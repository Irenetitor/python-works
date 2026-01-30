from pymongo import MongoClient
import os


#local database
db_client = MongoClient().local

#Remote database
#db_client = MongoClient("mongodb+srv://martincampoirene_db_user:28BYPkofzlM14nLu@cluster0.tpqq5io.mongodb.net/?appName=Cluster0").test

# MONGO_URI = os.getenv("MONGO_URI")
# db_client = MongoClient(MONGO_URI).test