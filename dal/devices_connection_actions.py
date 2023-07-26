from dal.crud_action import general_insert


async def insert(src_id, dest_id, protocol_type):
    query = "INSERT INTO  (src_id, dest_id, protocol_type) VALUES (%s, %s, %s)"
    return await general_insert(query, src_id, dest_id, protocol_type)
