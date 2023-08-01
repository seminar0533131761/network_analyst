import asyncio

from dal.crud_action import general_insert, general_get_multi_row_by_condition, get_row_by_condition, general_get_all
from dal.network_action import get_devices_by_network_id


async def get_all_devices_by_client_id(client_id):
    client_devices = []
    client_networks = await get_all_networks_by_client_id(client_id)
    for network in client_networks:
        devices = await get_devices_by_network_id(network["id"])
        if devices:
            client_devices.append(devices)
    return client_devices


async def get_all_networks_by_client_id(client_id):
    query = "SELECT * FROM network WHERE client_id = %s "
    return await general_get_multi_row_by_condition(query, client_id)


async def client_insert(_id, name):
    query = "INSERT INTO client (id, name) VALUES (%s,%s)"
    return await general_insert(query, _id, name)


async def is_client_connect_to_user(client_id, user_id):
    query = "SELECT * FROM client_user WHERE client_id=%s AND user_id=%s"
    return await get_row_by_condition(query, (client_id, user_id))
# asyncio.run(client_insert("1761", "baruch"))
# print(asyncio.run(get_all_networks(1761)))
# print(asyncio.run(get_all_devices_by_client_id(1761)))
# print(asyncio.run(general_get_all("SELECT * FROM client")))