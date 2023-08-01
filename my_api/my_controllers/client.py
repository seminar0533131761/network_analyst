from fastapi import APIRouter, Form, Depends

from dal.client_actions import get_all_devices_by_client_id
from my_modules.module_authentication import User, get_current_active_user

router = APIRouter()


# @router.get("/networks/{network_id}", response_model=dict)
# def get_network(network_id: int):
#     network = next((network for network in networks if network["id"] == network_id), None)
#     if not network:
#         raise HTTPException(status_code=404, detail="Network not found")
#     return network
#
#
# @router.post("/networks/", response_model=dict)
# def create_network(name: str, location: str):
#     new_network = {"id": len(networks) + 1, "name": name, "location": location}
#     networks.append(new_network)
#     return new_network

@router.get("/all_devices")
async def all_devices(client_id: int = Form(...), current_user: User = Depends(get_current_active_user)):
    devices = await get_all_devices_by_client_id(client_id)
    if devices:
        return devices
    return {"sorry": "we can can not find devices for this client"}

