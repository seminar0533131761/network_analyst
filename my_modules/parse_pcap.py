from io import BytesIO

from mac_vendor_lookup import AsyncMacLookup
from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.l2 import ARP
from scapy.layers.l2 import Ether


async def convert_context_to_lst_of_dicts(pcap_file_content):
    pcap_file = BytesIO(pcap_file_content)
    packets = rdpcap(pcap_file)
    packet_list = []

    # Process packets and extract information as needed
    for my_packet in packets:
        packet_dict = {}
        if IP in my_packet:
            packet_dict["source_ip"] = my_packet[IP].src
            packet_dict["destination_ip"] = my_packet[IP].dst
        else:
            # TODO: discover their ip address in another way
            packet_dict["source_ip"] = "unknown"
            packet_dict["destination_ip"] = "unknown"
        if Ether in my_packet:
            packet_dict["source_mac"] = my_packet[Ether].src
            packet_dict["destination_mac"] = my_packet[Ether].dst
            try:
                packet_dict["source_vendor"] = await AsyncMacLookup().lookup(packet_dict["source_mac"])
            except Exception as err:
                # TODO:  print ot log
                packet_dict["source_vendor"] = "unknown"
            try:
                packet_dict["destination_vendor"] = await AsyncMacLookup().lookup(packet_dict["destination_mac"])
            except Exception as err:
                # TODO:  print ot log
                packet_dict["destination_vendor"] = "unknown"
        if TCP in my_packet:
            packet_dict["protocol"] = "TCP"
        elif UDP in my_packet:
            packet_dict["protocol"] = "UDP"
        elif ICMP in my_packet:
            packet_dict["protocol"] = "ICMP"
        elif ARP in my_packet:
            packet_dict["protocol"] = "ARP"
        else:
            packet_dict["protocol"] = "Unknown"
        packet_list.append(packet_dict)

    return packet_list
