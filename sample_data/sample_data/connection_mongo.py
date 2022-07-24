import getpass
import pathlib

import pymongo
import json
from bson import ObjectId

connc_str = "mongodb://project2-cosmosdb:fkIRu6dlPW5kLN198Z1uHvddCSJpnjJIhcQaaT3acWaw8Ss3nUbeCBONKKWsA0CySUwtwYM3zK9V6kvm3Pw1Cw==@project2-cosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@project2-cosmosdb@"

DB_NAME = "projectdb"


def import_data(file_name: pathlib):
    json_file = open(file_name)
    json_list = json.load(json_file)
    return json_list


def main():
    """Connect to the API for MongoDB, create DB and collection, perform CRUD operations"""
    client = pymongo.MongoClient(connc_str)
    try:
        client.server_info()  # validate connection string
    except pymongo.errors.ServerSelectionTimeoutError:
        raise TimeoutError("Invalid API for MongoDB connection string or timed out when attempting to connect")
    collection_ads = client[DB_NAME].advertisement
    collection_posts = client[DB_NAME].post
    ads_list = import_data(file_name="./sampleAds.json")
    post_list = import_data(file_name="./samplePosts.json")

    # insert
    # insert_documents(collection_ads, ads_list)
    # insert_documents(collection_posts, post_list)

    # get
    _id = "5ec34b22c800f5f824c21490"
    query = {'_id': _id}
    result = collection_ads.find_one(query)
    print(result)
    return result


def insert_documents(collection, json_list: list):
    try:
        collection.insert_many(json_list)
    except Exception as e:
        print(f"Error occured while upserting in collection {collection} :: {e}")


if __name__ == '__main__':
    main()
