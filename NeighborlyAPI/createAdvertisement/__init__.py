import azure.functions as func
from mongoConnection import MongoConnection
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    request = req.get_json()

    if request:
        try:
            collection = MongoConnection(collection_name="advertisement").get_collection()

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )
