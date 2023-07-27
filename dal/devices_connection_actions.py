from dal.crud_action import general_insert, general_insert_many


async def insert(src_id, dest_id, protocol_type):
    query = "INSERT INTO  (src_id, dest_id, protocol_type) VALUES (%s, %s, %s)"
    return await general_insert(query, src_id, dest_id, protocol_type)


async def insert_many(lst_of_tuple):
    query = "insert INTO connection (src_id, dest_id, protocol_type) VALUES (%s, %s, %s)"
    return await general_insert_many(query, lst_of_tuple)
