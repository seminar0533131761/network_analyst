from dal.crud_action import general_get_multi_row_by_condition, general_insert


async def insert(subnet_musk, client_id, location):
    query = "INSERT INTO network (subnet_musk, client_id, location) VALUES (%s, %s, %s)"
    return await general_insert(query, subnet_musk, client_id, location)


async def get_devices_by_network_id(network_id):
    query = "SELECT * FROM devices WHERE network_id = %s"
    return await general_get_multi_row_by_condition(query, network_id)
