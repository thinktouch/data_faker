from pymongo import MongoClient
import pymongo

connect = MongoClient('localhost', 27017)
db = connect["es_mongodb_pk"]
collection = db["pk_pk"]

collection.create_index([("paragraph",pymongo.TEXT), ("mac_address", pymongo.TEXT)])
collection.create_index("name", unique=False)
collection.create_index("phone_number", unique=False)
collection.create_index("ip", unique=False)


def write_mongodb(data):
    collection.insert(data)