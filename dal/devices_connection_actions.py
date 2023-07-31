import asyncio

from dal.crud_action import general_insert, general_insert_many, general_delete_data, general_get_all


async def connection_insert(src_id, dest_id, protocol_type):
    query = "INSERT INTO connection (src_id, dest_id, protocol_type,network_id) VALUES (%s, %s, %s)"
    return await general_insert(query, src_id, dest_id, protocol_type)
    # reading_tuple = ("source_mac", "destination_mac", "source_ip", "destination_ip", "source_vendor"
    #                  , "destination_vendor", "protocol")


async def connection_insert_many(lst_of_dicts, network_id):
    query = "insert INTO connection (src_id, dest_id ,network_id,protocol_type) VALUES (%s, %s, %s,%s) "
    set_for_connections = set()
    for connection in lst_of_dicts:
        set_for_connections.add(
            (connection["source_mac"], connection["destination_mac"], network_id, connection["protocol"]))
    lst_for_connections = list(set_for_connections)
    return await general_insert_many(query, lst_for_connections)

# asyncio.run(general_delete_data("DELETE FROM connection"))
# print(asyncio.run(general_get_all("SELECT * FROM connection")))
