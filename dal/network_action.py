from connection import connectionObject
from dal.crud_action import general_get_multi_row_by_condition


async def get_devices_by_network_id(network_id):
    query = "SELECT * FROM devices WHERE network_id = %s"
    return await general_get_multi_row_by_condition(query, network_id)
