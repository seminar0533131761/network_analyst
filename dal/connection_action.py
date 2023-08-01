import asyncio

from dal.crud_action import general_get_all, general_get_multi_row_by_condition


# async def extract_files(network_id):
#     query = "SELECT src_id, dest_id FROM connection WHERE network_id = %s"
#     return await general_get_all(query, network_id)


# Extracts the connections according to the network_id and brings their details
async def extract_files(network_id):

    query = "SELECT src_id, dest_id FROM connection JOIN devices d1 WHERE d1.network_id = %s"
    return await general_get_all(query, network_id)
#Puts the source node and TUP of the target nodes into the dictionary (do it in the TUPEL to avoid duplication)
async def arrangement_of_connections(network_id):
    fetched_data = await extract_files(network_id)
    mapping_dict = {}
    for row in fetched_data:
        src_id = row['SRC_ID']
        dest_id = row['DEST_ID']
        if src_id in mapping_dict:
            mapping_dict[src_id].add(dest_id)
        else:
            mapping_dict[src_id] = {dest_id}

    query = "SELECT src_id, dest_id FROM connection JOIN device WHERE device.network_id = %s"
    return await general_get_multi_row_by_condition(query, network_id)
#>>>>>>> 1be86729fdc0a3e0184c30bcbdaaca32ad3cf816


# Puts the source node and TUPEL of the target nodes into the dictionary (do it in the TUPEL to avoid duplication)
# async def arrangement_of_connections(network_id):
#     fetched_data = await extract_files(network_id)
#     mapping_dict = {}
#     for row in fetched_data:
#         src_id = row['SRC_ID']
#         dest_id = row['DEST_ID']
#         if src_id in mapping_dict:
#             mapping_dict[src_id].add(dest_id)
#         else:
#             mapping_dict[src_id] = {dest_id}
#
#
# arrangement_of_connections(2)

# print(asyncio.run(extract_files(12)))