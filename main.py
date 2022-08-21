import requests
import logging.config

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator 


logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project. 
                                      # This will get the root logger since no logger in the configuration has this name.


app = FastAPI()

@app.get("/")
def read_root():
    response = api2()
    return {"AuthUsers": response }

@app.get("/authUsers/{internalId}")
def read_user(internalId : str):
    list=api2()
    for usr in list:
        print(usr)
        if usr["internalId"]==internalId:
            return usr
            

def api2():
    url='https://62fc67e61e6a530698a5ee17.mockapi.io/API2Taller1'
    response = requests.get(url, {}, timeout=5)
    return response.json()


Instrumentator().instrument(app).expose(app)

#@app.get("/")
#def read_root():
 #   url = 'https://62fc67e61e6a530698a5ee17.mockapi.io/API2Taller1'
 #   response = requests.get(url, {}, timeout=5)
 #   return {"items": response.json() }


#@app.get("/API2Taller1/{internalId}")
#def read_item(item_id: int, q: Union[str, None] = None):
 #   return {"item_id": item_id, "q": q}

