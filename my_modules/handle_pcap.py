from dal.device_actions import device_insert_many
from dal.devices_connection_actions import connection_insert_many
from dal.network_action import network_insert
from my_modules.parse_pcap import convert_context_to_lst_of_dicts


async def handle_file(file_content, network_info):
    data_lst_of_dicts = await convert_context_to_lst_of_dicts(file_content)
    return await update_db(data_lst_of_dicts, network_info)


async def update_db(data_lst_of_dicts, network_info):
    subnet_mask = "unknown"
    client_id = network_info["client_id"]
    location = network_info["location"]
    network_id = await network_insert(subnet_mask, client_id, location)
    if network_id:
        is_insertion_to_devices = await device_insert_many(data_lst_of_dicts, network_id)
        if is_insertion_to_devices:
            return await connection_insert_many(data_lst_of_dicts, network_id)
    else:
        return False
