import asyncio

from dal.crud_action import general_insert, general_insert_many, general_get_all


async def connection_insert(src_id, dest_id, protocol_type):
    query = "INSERT INTO connection (src_id, dest_id, protocol_type,network_id) VALUES (%s, %s, %s)"
    return await general_insert(query, src_id, dest_id, protocol_type)
    # reading_tuple = ("source_mac", "destination_mac", "source_ip", "destination_ip", "source_vendor"
    #                  , "destination_vendor", "protocol")


async def connection_insert_many(lst_of_dicts, network_id):
    # query = "insert INTO connection (src_id, dest_id, protocol_type,network_id) VALUES (%s, %s, %s) "
    # query = "INSERT INTO connection (src_id, dest_id, protocol_type, network_id) SELECT %s, %s, %s, %s WHERE NOT EXISTS" \
    #         "(SELECT src_id FROM connection WHERE src_id = %s AND dest_id = %s AND protocol_type = %s AND network_id " \
    #         "= %s)"
    query = "insert INTO connection (src_id, dest_id ,network_id,protocol_type) VALUES (%s, %s, %s,%s) "
    lst_for_connections = []
    # the slicing is because connection table needs only this data
    # print("lst_of_dicts", lst_of_dicts[:6])
    for connection in lst_of_dicts:
        lst_for_connections.append(
            (connection["source_mac"], connection["destination_mac"], network_id, connection["protocol"]))
    print("connection lst of tuples", lst_for_connections[:3])
    return await general_insert_many(query, lst_for_connections)


# asyncio.run(general_delete_data("DELETE FROM connection"))

print(asyncio.run(general_get_all("SELECT * FROM connection")))
