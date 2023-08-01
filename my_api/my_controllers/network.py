from fastapi import APIRouter, Depends, Form
from dal.device_actions import get_all_network_devices_by_protocol_type
from my_modules.module_authentication import User, get_current_active_user

router = APIRouter()


@router.get("/get-device-by-protocol")
async def get_device_by_protocol_type(network_id: int, protocol_type: str,
                                      current_user: User = Depends(get_current_active_user)):
    return await get_all_network_devices_by_protocol_type(network_id, protocol_type)
