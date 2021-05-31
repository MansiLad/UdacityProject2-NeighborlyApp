import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://neighborlyproject:8pvDTQa1eCCRExhO2EhbrA09czsFfkrNhPW4ZdE45rpa8v8LgtcsEP1nBUh6AtdgJNj8ENi38Kqs7Z1fQC4yFQ==@neighborlyproject.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlyproject@"
        client = pymongo.MongoClient(url)
        database = client['project2']
        collection = database['advertisements']
        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

