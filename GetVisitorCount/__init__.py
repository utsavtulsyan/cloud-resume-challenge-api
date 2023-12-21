import logging
import json
import azure.functions as func
from azure.data.tables import TableClient, UpdateMode
import os

def main(req: func.HttpRequest, userCount) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    userCountJson = json.loads(userCount)
    userCountJson[0]['count'] += 1 
    with TableClient.from_connection_string(
        conn_str=os.environ["AzureWebJobsStorage"], table_name="resume"
   ) as table_client:
        table_client.update_entity(mode=UpdateMode.REPLACE, entity=userCountJson[0])
        logging.info('count update successful!')

    return func.HttpResponse(str(userCountJson[0]['count']))

