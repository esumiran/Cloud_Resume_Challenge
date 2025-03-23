import azure.functions as func
import logging
import os
import json
from pymongo import MongoClient

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

CosmosDB_ConnectionString = os.getenv("CosmosDB_ConnectionString")
CosmosDB_name = os.getenv("CosmosDB_name")
CosmosDB_Collection_name = os.getenv("CosmosDB_Collection_name")

client = MongoClient(CosmosDB_ConnectionString)

db = client[CosmosDB_name]
collection = db[CosmosDB_Collection_name]


@app.route(route="GetResumeCount")
def GetResumeCount(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        # Query to fetch the visitor count record (assuming there's only one document)
        client = MongoClient(CosmosDB_ConnectionString)

        db = client[CosmosDB_name]
        collection = db[CosmosDB_Collection_name]

        visitor_count_record = collection.find_one({"id": "1"})
        
        if visitor_count_record:
            count = int(visitor_count_record["visitor_count"])
            response_data = {"visitor_count": count}
            count = count + 1 

            # Update the visitor count in the database
            collection.update_one({"id": "1"}, {"$set": {"visitor_count": count}})
            response_data["visitor_count"] = count
        else:
            # If no count exists, create a new record
            new_item = {"id": "1", "visitor_count": 1}
            collection.insert_one(new_item)
            response_data = {"visitor_count": 1}

        return func.HttpResponse(json.dumps(response_data), mimetype="application/json")

    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            mimetype="application/json",
            status_code=500
        )