import logging
import json
import azure.functions as func
from azure.data.tables import TableClient, UpdateMode
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        with TableClient.from_connection_string(
            conn_str=os.environ["AzureWebJobsStorage"], table_name="resume"
    ) as table_client:
            
            userCountJson = table_client.get_entity("", "")
            userCountJson['count'] += 1 
            table_client.update_entity(mode=UpdateMode.REPLACE, entity=userCountJson)
            logging.info('count update successful!')
            return func.HttpResponse(str(userCountJson['count']))
    except Exception as e:
        logging.error('Failed with error: %s', e)
        return func.HttpResponse('internal error', status_code=500)



