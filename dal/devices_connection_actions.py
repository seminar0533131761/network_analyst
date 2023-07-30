from dal.crud_action import general_insert, general_insert_many


async def connection_insert(src_id, dest_id, protocol_type):
    query = "INSERT INTO connection (src_id, dest_id, protocol_type,network_id) VALUES (%s, %s, %s)"
    return await general_insert(query, src_id, dest_id, protocol_type)
    # reading_tuple = ("source_mac", "destination_mac", "source_ip", "destination_ip", "source_vendor"
    #                  , "destination_vendor", "protocol")


async def connection_insert_many(lst_of_dicts, network_id):
    # query = "insert INTO connection (src_id, dest_id, protocol_type,network_id) VALUES (%s, %s, %s) "
    query = "INSERT INTO connection (src_id, dest_id, protocol_type, network_id) SELECT %s, %s, %s, %s WHERE NOT EXISTS" \
            "(SELECT src_id FROM connection WHERE src_id = %s AND dest_id = %s AND protocol_type = %s AND network_id " \
            "= %s)"
    lst_for_connections = []
    # the slicing is because connection table needs only this data
    for connection in lst_of_dicts:
        lst_for_connections.append((connection["src_id"],connection["dest_id"],connection["protocol"],network_id))
    return await general_insert_many(query, lst_for_connections)

