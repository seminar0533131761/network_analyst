data = {
    "00:50:56:c0:00:02": {
        "devices": {
            "00:0c:29:1f:f8:1a": {
                "protocol_type": [
                    "TCP"
                ],
                "dest_ip_address": "192.168.1.157",
                "vendor": "VMware, Inc."
            },
            "00:0c:29:69:e6:2b": {
                "protocol_type": [
                    "TCP"
                ],
                "dest_ip_address": "192.168.1.30",
                "vendor": "VMware, Inc."
            },
            "ff:ff:ff:ff:ff:ff": {
                "protocol_type": [
                    "ARP"
                ],
                "dest_ip_address": "192.168.1.255",
                "vendor": "unknown"
            }
        }
    },
    "00:12:79:45:a4:bb": {
        "devices": {
            "00:0c:29:b0:8d:62": {
                "protocol_type": [
                    "TCP",
                    "UDP",
                    "ARP"
                ],
                "dest_ip_address": "unknown",
                "vendor": "VMware, Inc."
            },
            "01:00:5e:7f:ff:fa": {
                "protocol_type": [
                    "UDP"
                ],
                "dest_ip_address": "239.255.255.250",
                "vendor": "unknown"
            },
            "00:21:70:4d:4f:ae": {
                "protocol_type": [
                    "TCP",
                    "ARP"
                ],
                "dest_ip_address": "unknown",
                "vendor": "Dell Inc."
            }
        }
    },
    "00:0c:29:b0:8d:62": {
        "devices": {
            "ff:ff:ff:ff:ff:ff": {
                "protocol_type": [
                    "UDP"
                ],
                "dest_ip_address": "192.168.1.255",
                "vendor": "unknown"
            },
            "00:0c:29:69:e6:2b": {
                "protocol_type": [
                    "UDP",
                    "ARP"
                ],
                "dest_ip_address": "192.168.1.30",
                "vendor": "VMware, Inc."
            },
            "00:12:79:45:a4:bb": {
                "protocol_type": [
                    "TCP",
                    "UDP",
                    "ARP"
                ],
                "dest_ip_address": "192.168.1.158",
                "vendor": "Hewlett Packard"
            },
            "00:21:70:4d:4f:ae": {
                "protocol_type": [
                    "TCP",
                    "UDP",
                    "ARP"
                ],
                "dest_ip_address": "unknown",
                "vendor": "Dell Inc."
            }
        }
    },
    "00:21:70:4d:4f:ae": {
        "devices": {
            "ff:ff:ff:ff:ff:ff": {
                "protocol_type": [
                    "UDP",
                    "ARP"
                ],
                "dest_ip_address": "192.168.1.255",
                "vendor": "unknown"
            },
            "00:0c:29:b0:8d:62": {
                "protocol_type": [
                    "TCP",
                    "UDP",
                    "ARP"
                ],
                "dest_ip_address": "unknown",
                "vendor": "VMware, Inc."
            },
            "00:12:79:45:a4:bb": {
                "protocol_type": [
                    "TCP"
                ],
                "dest_ip_address": "192.168.1.158",
                "vendor": "Hewlett Packard"
            }
        }
    },
    "00:0c:29:69:e6:2b": {
        "devices": {
            "00:0c:29:b0:8d:62": {
                "protocol_type": [
                    "UDP",
                    "ARP"
                ],
                "dest_ip_address": "unknown",
                "vendor": "VMware, Inc."
            },
            "00:50:56:c0:00:02": {
                "protocol_type": [
                    "TCP"
                ],
                "dest_ip_address": "192.168.1.2",
                "vendor": "VMware, Inc."
            }
        }
    },
    "00:0c:29:1f:f8:1a": {
        "devices": {
            "ff:ff:ff:ff:ff:ff": {
                "protocol_type": [
                    "UDP"
                ],
                "dest_ip_address": "192.168.1.255",
                "vendor": "unknown"
            },
            "00:50:56:c0:00:02": {
                "protocol_type": [
                    "TCP",
                    "ARP"
                ],
                "dest_ip_address": "192.168.1.2",
                "vendor": "VMware, Inc."
            }
        }
    }
}

# # Create a dictionary to store the count of packets received by each MAC address
# packet_count = defaultdict(int)
#
# # Iterate through the data and count the packets for each MAC address
# for source_mac, info in data.items():
#     print(info)
#     for dest_mac in info['devices']:
#         packet_count[dest_mac] += len(info['devices'][dest_mac]['protocol_type'])
#
# # Find the MAC address with the highest packet count
# most_traffic_mac = max(packet_count, key=packet_count.get)
#
# # Print the MAC address of the router
# print("Router MAC Address:", most_traffic_mac)

mac_and_count_ip = dict()


async def find_the_router(dict_of_data):
    for source_mac, info in data.items():
        print(info)
        for dest_mac in info['devices']:
            if dest_mac in mac_and_count_ip[dest_mac]:
                mac_and_count_ip[dest_mac].add(info["devices"]["dest_mac"]["dest_ip_address"])
            else:
                # mac_and_count_ip[dest_]
                mac_and_count_ip[dest_mac] = info["devices"]["dest_mac"]["dest_ip_address"]
            # mac_and_count_ip[dest_mac] += len(info['devices'][dest_mac]['protocol_type'])
