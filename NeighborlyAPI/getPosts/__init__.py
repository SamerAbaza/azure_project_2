import logging
import azure.functions as func
from bson.json_util import dumps


from mongoConnection import MongoConnection


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python getPosts trigger function processed a request.')

    try:
        collection = MongoConnection(collection_name="post").get_collection()
        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except Exception as e:
        return func.HttpResponse(f"Bad request.{e}", status_code=400)