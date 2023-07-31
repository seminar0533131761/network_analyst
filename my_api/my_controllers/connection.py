from fastapi import APIRouter, Depends, Form

from dal.devices_connection_actions import get_connections
from my_modules.module_authentication import User, get_current_active_user

router = APIRouter()


# get the connections of the devices (still MTH)
@router.get("/network_mapping")
async def network_mapping(network_id: int = Form(...), current_user: User = Depends(get_current_active_user))
    print(network_id)
    return await get_connections(network_id)
