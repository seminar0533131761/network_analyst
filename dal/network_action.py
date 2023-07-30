from dal.crud_action import general_get_multi_row_by_condition, general_insert, general_delete_data


async def network_insert(subnet_mask, client_id, location):
    query = "INSERT INTO network (subnet_musk, client_id, location) VALUES (%s, %s, %s)"
    print("in network :", client_id, location)
    return await general_insert(query, subnet_mask, client_id, location)


async def network_delete(query):
    return await general_delete_data(query)


async def get_devices_by_network_id(network_id):
    query = "SELECT * FROM devices WHERE network_id = %s"
    return await general_get_multi_row_by_condition(query, network_id)

# asyncio.run(network_delete("DELETE FROM network"))
# print(asyncio.run(general_get_all("SELECT * FROM network")))
