import logging

from fastapi import APIRouter, Form, Depends

from dal.client_actions import get_all_devices_by_client_id, get_all_networks_by_client_id
from my_modules.module_authentication import User, get_current_active_user
from self_logging import MyLogger

router = APIRouter()
my_logger = MyLogger(log_level=logging.INFO)
logger = my_logger.get_logger()


@router.get("/all-networks")
async def get_all_networks(client_id: str = Form(...), current_user: User = Depends(get_current_active_user)):
    networks = await get_all_networks_by_client_id(client_id)
    if networks:
        return networks
    msg = "we can can not find networks for this client"
    logger.info(msg)
    return {"sorry": msg}


@router.get("/all-devices")
async def all_devices(client_id: int = Form(...), current_user: User = Depends(get_current_active_user)):
    devices = await get_all_devices_by_client_id(client_id)
    if devices:
        return devices
    msg = "we can can not find devices for this client"
    logger.info(msg)
    return {"sorry": "we can can not find devices for this client"}
