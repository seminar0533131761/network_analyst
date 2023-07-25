from connection import connectionObject

async def get_devices_by_network_id(id):
    try:
        with connectionObject.cursor() as cursor:
            network_id = 'your_network_id'
            sql_query = "SELECT * FROM devices WHERE network_id = %s"
            cursor.execute(sql_query, (network_id,))
            devices = cursor.fetchall()
            return devices
            connectionObject.commit()
    except Exception as err:
        print(err)
        return False
    finally:
        connectionObject.close()
