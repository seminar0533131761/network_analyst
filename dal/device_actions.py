from dal.crud_action import general_insert


async def insert(device_type, vendor, network_id, ip_address):
    query = "INSERT INTO device (device_type, vendor, network_id, ip_address) VALUES (%s, %s, %s, %s)"
    return await general_insert(query, device_type, vendor, network_id, ip_address)

