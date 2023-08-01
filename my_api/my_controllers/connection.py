import logging

from fastapi import APIRouter, Depends, Form, Response, Path

from dal.devices_connection_actions import get_connections
from my_modules.connection_visualization import plot_connections
from my_modules.module_authentication import User, get_current_active_user
from my_modules.self_logging import MyLogger

router = APIRouter()
my_logger = MyLogger(log_level=logging.INFO)
logger = my_logger.get_logger()


# get the connections of the devices (still MTH)
@router.get("/network_mapping")
async def network_mapping(network_id: int = Form(...),
                          current_user: User = Depends(get_current_active_user)):
    connections = await get_connections(network_id)
    if connections:
        return connections
    msg = "could not get the connections, check again your data"
    logger.info(msg)
    return {"sorry": msg}


@router.get("/network-mapping-visualization/{network_id}")
# TODO : with authentication
# current_user: User = Depends(get_current_active_user)
async def network_mapping_visualization(network_id: int = Path(...)):
    connections = await get_connections(network_id)
    if connections:
        buffer = await plot_connections(connections)
        response = Response(content=buffer.getvalue(), media_type="image/png")
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = 'O'
        return response
    msg = f"no connections found for {network_id}"
    logger.info(msg)
    return {"sorry": msg}



