import asyncio

from dal.crud_action import get_row_by_condition, general_insert
from dal.network_action import get_devices_by_network_id


async def get_all_devices_by_client_id(client_id):
    client_devices = []
    client_networks = await get_all_networks(client_id)
    for network in client_networks:
        client_devices.append(await get_devices_by_network_id(network["id"]))


async def get_all_networks(client_id):
    query = "SELECT * FROM network WHERE client_id = %s"
    return await get_row_by_condition(query, client_id)


async def client_insert(_id, name):
    query = "INSERT INTO client (id, name) VALUES (%s,%s)"
    return await general_insert(query, _id, name)


# asyncio.run(client_insert("1761", "baruch"))
