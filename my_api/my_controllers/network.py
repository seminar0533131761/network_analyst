import logging

from fastapi import APIRouter, Depends

from dal.device_actions import get_all_network_devices_by_protocol_type
from my_modules.module_authentication import User, get_current_active_user
from my_modules.self_logging import MyLogger

router = APIRouter()
my_logger = MyLogger(log_level=logging.INFO)
logger = my_logger.get_logger()


@router.get("/get-device-by-protocol")
async def get_device_by_protocol_type(network_id: int = None, protocol_type: str = None,
                                      current_user: User = Depends(get_current_active_user)):
    if network_id and protocol_type:
        devices = await get_all_network_devices_by_protocol_type(network_id, protocol_type)
        if devices:
            return devices
        logger.info(f"no devices found for network: {network_id} with protocol type {protocol_type}")
        return {"sorry": "no devices found check again your data"}
    return {"sorry": "no filters given"}
