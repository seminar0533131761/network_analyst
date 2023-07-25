from fastapi import APIRouter, HTTPException

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
