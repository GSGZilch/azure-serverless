import logging
import json

import azure.functions as func


def main(req: func.HttpRequest, documents: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    user_id = req.params.get('userId')

    ratings_json = []

    for rating in documents:
        if rating['userId'] == user_id:
            ratings_json = {
                "id": rating['id'],
                "name": rating['name'],
                # get all attributes
            }
    ratings_json.append(ratings_json)

    if user_id:
        return func.HttpResponse(
                json.dumps(ratings_json),
                status_code=200,
                mimetype="application/json"            
        )
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a userId in the query string or in the request body for a personalized response.",
             status_code=200
        )