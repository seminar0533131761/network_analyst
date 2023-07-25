from dal.crud_action import get_row_by_condition
from dal.network_action import get_devices_by_network_id


async def get_all_devices_by_client_id(client_id, get_devices_by_network_idgenetwork=None):
    client_devices=[]
    client_network = await get_all_networks(client_id)
    for network in client_network:
        client_devices.append(await get_devices_by_network_id(network["id"]))



async def get_all_networks(client_id):
    query = "SELECT * FROM network WHERE client_id = %s"
    return await get_row_by_condition(query, client_id)
