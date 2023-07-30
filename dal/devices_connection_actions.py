from dal.crud_action import general_insert, general_insert_many


async def insert(src_id, dest_id, protocol_type):
    query = "INSERT INTO  (src_id, dest_id, protocol_type,network_id) VALUES (%s, %s, %s)"
    return await general_insert(query, src_id, dest_id, protocol_type)
    # reading_tuple = ("source_mac", "destination_mac", "source_ip", "destination_ip", "source_vendor"
    #                  , "destination_vendor", "protocol")


async def insert_many(lst_of_tuple, network_id):
    query = "insert INTO connection (src_id, dest_id, protocol_type,network_id) VALUES (%s, %s, %s) "
    # the slicing is because connection table needs only this data
    lst_for_connections = lst_of_tuple[:3] + (network_id,)
    return await general_insert_many(query, lst_for_connections)
