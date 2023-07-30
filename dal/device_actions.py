from dal.crud_action import general_insert


async def device_insert(device_type, vendor, network_id, ip_address):
    query = "INSERT INTO device (device_type, vendor, network_id, ip_address) VALUES (%s, %s, %s, %s)"
    return await general_insert(query, device_type, vendor, network_id, ip_address)


async def device_insert_many(lst_of_tuple, network_id):
    query = "INSERT INTO device (id, device_type, vendor, network_id, ip_address) VALUES (%s, %s, %s, %s, %s) " \
            "ON DUPLICATE KEY UPDATE device_type=VALUES(device_type), vendor=VALUES(vendor), network_id=VALUES(network_id), ip_address=VALUES(ip_address)"
    devices_lst_of_tuples = []
    for connection in lst_of_tuple:
        devices_lst_of_tuples.append((connection["source_mac"], "no device type ", connection["vendor"]
                                      , connection["network_id"], connection["ip_address"]))

# return await general_insert_many(query, lst_for_connections)
