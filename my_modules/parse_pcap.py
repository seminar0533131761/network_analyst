from io import BytesIO

from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.l2 import Ether
from mac_vendor_lookup import MacLookup
# fix it

mac = MacLookup()


async def handle_file(file_content):
    data_lst_of_dicts = await convert_context_to_lst_of_dicts(file_content)
    await update_db(data_lst_of_dicts)


async def convert_context_to_lst_of_dicts(pcap_file_content):
    pcap_file = BytesIO(pcap_file_content)
    packets = rdpcap(pcap_file)
    packet_list = []

    # Process packets and extract information as needed
    for my_packet in packets[:6]:
        packet_dict = {}
        if IP in my_packet:
            packet_dict["source_ip"] = my_packet[IP].src
            packet_dict["destination_ip"] = my_packet[IP].dst
        if Ether in my_packet:
            packet_dict["source_mac"] = my_packet[Ether].src
            packet_dict["destination_mac"] = my_packet[Ether].dst
            # here
            # packet_dict["vendor"] = await mac.lookup(packet_dict["source_mac"])
        if TCP in my_packet:
            packet_dict["protocol"] = "TCP"
        elif UDP in my_packet:
            packet_dict["protocol"] = "UDP"
        elif ICMP in my_packet:
            packet_dict["protocol"] = "ICMP"
        else:
            packet_dict["protocol"] = "Unknown"
        packet_list.append(packet_dict)

    return packet_list


async def update_db(data_lst_of_dicts):
    data_lst_of_tuples = []
    ids_lst = []
    # because the syntax of pymysql is list_of_dicts and list_of_dicts was gotten
    for data_dict in data_lst_of_dicts:
        data_lst_of_tuples.append((data_dict['source_mac'], data_dict['destination_mac'],))
