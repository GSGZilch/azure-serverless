import logging

import azure.functions as func


def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    id = req.params.get('id'),
    userId = req.params.get('userId')

    if not id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            id = req_body.get('id'),
            userId = req_body.get('userId')

    if id:
        newratings = func.DocumentList() 
        newrating_dict = {
            "id": id,
            "userId": userId
        }

        newratings.append(func.Document.from_dict(newrating_dict))
        doc.set(newratings)
        return func.HttpResponse(f"Hello, {userId}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
