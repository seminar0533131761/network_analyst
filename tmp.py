from collections import defaultdict


async def find_the_router(data_dict):
    # Create a dictionary to store the count of packets received by each MAC address
    packet_count = defaultdict(int)

    # Iterate through the data and count the packets for each MAC address
    for source_mac, info in data_dict.items():
        for dest_mac in info['devices']:
            packet_count[dest_mac] += len(info['devices'][dest_mac]['protocol_type'])

    # Find the MAC address with the highest packet count
    most_traffic_mac = max(packet_count, key=packet_count.get)

    # Print the MAC address of the router
    return {"router_mac_address": most_traffic_mac}
