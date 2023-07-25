from connection import connectionObject
from network_action import get_devices_by_network_id
async def get_all_devices_by_client_id():
    network_ids = []
    client_network = get_all_networks()
    for network in client_network:
        network_ids.append(network["id"])
    for i in network_ids:
        get_all_networks(i)



async def get_all_networks():

            sql_query = "SELECT * FROM network WHERE client_id = %s"
            cursor.execute(sql_query, (client_id,))
            network = cursor.fetchall()
            return network
            connectionObject.commit()
    except Exception as err:
        print(err)
        return False
    finally:
        connectionObject.close()

