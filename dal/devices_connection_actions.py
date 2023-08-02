

from dal.crud_action import general_insert, general_insert_many, general_get_multi_row_by_condition


async def connection_insert(src_id, dest_id, protocol_type):
    query = "INSERT INTO connection (src_id, dest_id, protocol_type,network_id) VALUES (%s, %s, %s)"
    return await general_insert(query, src_id, dest_id, protocol_type)


async def connection_insert_many(lst_of_dicts, network_id):
    query = "insert INTO connection (src_id, dest_id ,network_id,protocol_type) VALUES (%s, %s, %s,%s) "
    # the set is because we want to avoid duplicates rows in all fields
    set_for_connections = set()
    for connection in lst_of_dicts:
        set_for_connections.add(
            (connection["source_mac"], connection["destination_mac"], network_id, connection["protocol"]))
    lst_for_connections = list(set_for_connections)
    return await general_insert_many(query, lst_for_connections)


# async def get_connections(network_id):
#     device_query = "SELECT * FROM device WHERE network_id = %s "
#     lst_of_devices = await general_get_multi_row_by_condition(device_query, network_id)
#     connection_query = "SELECT src_id, dest_id FROM connection WHERE connection.network_id = %s "
#     lst_of_connections = await general_get_multi_row_by_condition(connection_query, network_id)
#     # creating of dict which will have mac as key and dict as value the dict will contain
#     # devices=lst of devices communicated with this devices
#     dict_of_connection_map = {}
#     for item in lst_of_connections:
#         print("item", item)
#         if item["src_id"] in dict_of_connection_map.keys():
#             if not item["dest_id"] in dict_of_connection_map[item["src_id"]]:
#                 dict_of_connection_map[item["src_id"]]["devices"].append(item["dest_id"])
#         else:
#             dict_of_connection_map[item["src_id"]] = {"devices": []}
#             dict_of_connection_map[item["src_id"]]["devices"].append(item["dest_id"])
#     return await add_vendor(dict_of_connection_map, lst_of_devices)
#
#
# # the purpose is to add to each device the vendor
# async def add_vendor(dict_of_connection_map, lst_of_devices):
#     for mac in dict_of_connection_map.keys():
#         for device in lst_of_devices:
#             if device["id"] == mac:
#                 # as explained in the former function I have dict with keys each key represent
#                 # mac address and the value is dict which has devices=lst of devices communicated with this devices
#                 # from the former function and adding new field vendor
#                 dict_of_connection_map[mac]["vendor"] = device["vendor"]
#     return dict_of_connection_map

# asyncio.run(general_delete_data("DELETE FROM connection"))
# print(asyncio.run(general_get_all("SELECT * FROM connection")))


async def get_connections(network_id):
    connection_query = (
        "SELECT device.id as dest_id, connection.src_id, device.vendor, connection.protocol_type, device.ip_address "
        "FROM device "
        "JOIN connection "
        "ON connection.dest_id = device.id "
        "WHERE connection.network_id = %s"
    )

    lst_of_connections = await general_get_multi_row_by_condition(connection_query, network_id)
    # creating of dict which will have mac as key and dict as value the dict will contain
    # devices=lst of devices communicated with this devices
    dict_of_connection_map = {}
    for item in lst_of_connections:
        if item["src_id"] in dict_of_connection_map:
            if item["dest_id"] in dict_of_connection_map[item["src_id"]]["devices"].keys():
                dict_of_connection_map[item["src_id"]]["devices"][item["dest_id"]]["protocol_type"].add(item["protocol_type"])
            else:
                dict_of_connection_map[item["src_id"]]["devices"][item["dest_id"]]= {
                    "protocol_type": set(),
                    "ip_address": item["ip_address"],
                    "vendor": item["vendor"]
                }
                dict_of_connection_map[item["src_id"]]["devices"][item["dest_id"]]["protocol_type"].add(item["protocol_type"])

        else:
<<<<<<< HEAD
            dict_of_connection_map[item["src_id"]] = {
                "devices": {
                    item["dest_id"]: {
                        "protocol_type": set(),
                        "ip_address": item["ip_address"],
                        "vendor": item["vendor"]
                    }
                }
            }
            dict_of_connection_map[item["src_id"]]["devices"][item["dest_id"]]["protocol_type"].add(
                item["protocol_type"])
    return dict_of_connection_map




# asyncio.run(get_connections_for_visualization(12))
=======
            dict_of_connection_map[item["src_id"]] = {"devices": []}
            dict_of_connection_map[item["src_id"]]["devices"].append(item["dest_id"])
    return await add_vendor(dict_of_connection_map, lst_of_devices)


# the purpose is to add to each device the vendor
async def add_vendor(dict_of_connection_map, lst_of_devices):
    for mac in dict_of_connection_map.keys():
        for device in lst_of_devices:
            if device["id"] == mac:
                # as explained in the former function I have dict with keys each key represent
                # mac address and the value is dict which has devices=lst of devices communicated with this devices
                # from the former function and adding new field vendor
                dict_of_connection_map[mac]["vendor"] = device["vendor"]
    return dict_of_connection_map

>>>>>>> origin/main
