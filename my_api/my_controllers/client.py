from fastapi import APIRouter, Form, Depends
from dal.client_actions import get_all_devices_by_client_id, get_all_networks_by_client_id
from my_modules.module_authentication import User, get_current_active_user

router = APIRouter()

@router.get("/all-networks")
async def get_all_networks(client_id: str = Form(...) , current_user: User = Depends(get_current_active_user)):
    return await get_all_networks_by_client_id(client_id)

@router.get("/all_devices")
async def all_devices(client_id: int = Form(...), current_user: User = Depends(get_current_active_user)):
    devices = await get_all_devices_by_client_id(client_id)
    if devices:
        return devices
    return {"sorry": "we can can not find devices for this client"}

