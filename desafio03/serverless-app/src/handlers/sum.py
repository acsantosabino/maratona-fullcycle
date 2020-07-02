import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    a = req.params.get('a')
    b = req.params.get('b')

    if a and b:
        valor = int(a)+int(b)
        jsonObj = {
            "resultado": valor
            }
        return func.HttpResponse(body=json.dumps(jsonObj), mimetype='application/json')
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )