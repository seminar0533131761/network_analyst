import os
import sys

import uvicorn

# to make sys search from network_analyst not from my_api
curr_path = os.path.dirname(__file__)
root_path = os.path.join(curr_path, "..")
sys.path.append(root_path)

from fastapi import FastAPI
from my_controllers.user import router as user_router
# from my_controllers.network import router as network_router
from my_controllers.client import router as client_router
from my_controllers.cap import router as cap_router
from my_controllers.connection import router as connection_router
from my_controllers.authentication import router as authentication_router

app = FastAPI()

# gather all routes
app.include_router(user_router, prefix="/users", tags=["users"])
# app.include_router(network_router, prefix="/networks", tags=["networks"])
app.include_router(client_router, prefix="/clients", tags=["clients"])
app.include_router(cap_router, prefix="/caps", tags=["caps"])
app.include_router(connection_router, prefix="/connections", tags=["connections"])
app.include_router(authentication_router, prefix="/authentication", tags=["authentication"])

uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
