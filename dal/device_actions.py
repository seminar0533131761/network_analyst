from dal.crud_action import general_insert, general_insert_many


async def device_insert(device_type, vendor, network_id, ip_address):
    query = "INSERT INTO device (device_type, vendor, network_id, ip_address) VALUES (%s, %s, %s, %s)"
    return await general_insert(query, device_type, vendor, network_id, ip_address)


async def device_insert_many(lst_of_dicts, network_id):
    print("got to device insert")
    query = "INSERT IGNORE INTO device (id, device_type, vendor, network_id, ip_address) VALUES (%s, %s, %s, %s, %s)"
    devices_lst_of_tuples = []
    print("lst_of_dicts", lst_of_dicts[:2])
    for connection in lst_of_dicts:
        devices_lst_of_tuples.append((connection["source_mac"], "no device type ", connection["source_vendor"]
                                      , network_id, connection["source_ip"]))
        devices_lst_of_tuples.append((connection["destination_mac"], "no device type ", connection["destination_vendor"]
                                      , network_id, connection["destination_ip"]))
    return await general_insert_many(query, devices_lst_of_tuples)
