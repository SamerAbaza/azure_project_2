import azure.functions as func

from bson.objectid import ObjectId
import os

from mongoConnection import MongoConnection


def main(req: func.HttpRequest) -> func.HttpResponse:
    id = req.params.get('id')

    if id:
        try:
            collection = MongoConnection(collection_name="advertisement").get_collection()
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
