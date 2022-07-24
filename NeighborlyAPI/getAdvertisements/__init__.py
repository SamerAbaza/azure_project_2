import azure.functions as func
from bson.json_util import dumps

from mongoConnection import MongoConnection


def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        collection = MongoConnection(collection_name="advertisement").get_collection()
        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

