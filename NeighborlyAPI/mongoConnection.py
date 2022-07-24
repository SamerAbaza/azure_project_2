import pymongo


class MongoConnection:
    def __init__(self, collection_name):
        db_name = "projectdb"
        conn_str = "mongodb://project2-cosmosdb:fkIRu6dlPW5kLN198Z1uHvddCSJpnjJIhcQaaT3acWaw8Ss3nUbeCBONKKWsA0CySUwtwYM3zK9V6kvm3Pw1Cw==@project2-cosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@project2-cosmosdb@"
        client = pymongo.MongoClient(conn_str)
        self.database = client[db_name]
        self.collection = self.database[collection_name]

    def get_collection(self):
        return self.collection
