from dal.device_actions import device_insert_many
from dal.devices_connection_actions import connection_insert_many
from dal.network_action import network_insert
from my_modules.parse_pcap import convert_context_to_lst_of_dicts


async def handle_file(file_content, network_info):
    data_lst_of_dicts = await convert_context_to_lst_of_dicts(file_content)
    await update_db(data_lst_of_dicts, network_info)


async def update_db(data_lst_of_dicts, network_info):
    # represent what each line is
    # data_lst_of_tuples = []
    # ids_lst = []
    # # because the syntax of pymysql is list_of_dicts and list_of_dicts was gotten
    # for data_dict in data_lst_of_dicts:
    #     data_lst_of_tuples.append(
    #         (data_dict['source_mac'], data_dict['destination_mac'], data_dict["protocol"], data_dict["source_ip"],
    #          data_dict["destination_ip"], data_dict["source_vendor"],
    #          data_dict["destination_vendor"]
    #          ))
    subnet_mask = "unknown"
    client_id = network_info["client_id"]
    location = network_info["location"]
    network_id = await network_insert(subnet_mask, client_id, location)
    is_insertion_to_connection = await connection_insert_many(data_lst_of_dicts, network_id)
    if is_insertion_to_connection:
        await device_insert_many(data_lst_of_dicts, network_id)
#     TODO: handle devices
