from io import BytesIO

from mac_vendor_lookup import AsyncMacLookup
from scapy.all import *

from my_modules.self_logging import MyLogger

my_logger = MyLogger(log_level=logging.INFO)
logger = my_logger.get_logger()


# the 2 following functions represent the abstraction ideal whether the data comes as json xml or
# it will also be handled

async def convert_pcap_to_lst_of_dicts(pcap_file_content):
    pcap_file = BytesIO(pcap_file_content)
    packets = rdpcap(pcap_file)
    return await process_packets(packets)


async def process_packets(packets):
    packet_list = []
    for my_packet in packets:
        packet_dict = {}
        if "ip" in my_packet:
            packet_dict["source_ip"] = my_packet["ip"]["src"]
            packet_dict["destination_ip"] = my_packet["ip"]["dst"]
        else:
            packet_dict["source_ip"] = "unknown"
            packet_dict["destination_ip"] = "unknown"

        if "ether" in my_packet:
            packet_dict["source_mac"] = my_packet["ether"]["src"]
            packet_dict["destination_mac"] = my_packet["ether"]["dst"]
            try:
                packet_dict["source_vendor"] = await AsyncMacLookup().lookup(packet_dict["source_mac"])
            except Exception as err:
                logger.error("error!!!", err)
                packet_dict["source_vendor"] = "unknown"
            try:
                packet_dict["destination_vendor"] = await AsyncMacLookup().lookup(packet_dict["destination_mac"])
            except Exception as err:
                logger.error("error!!!", err)
                packet_dict["destination_vendor"] = "unknown"

        if "protocol" in my_packet:
            packet_dict["protocol"] = my_packet["protocol"]
        else:
            packet_dict["protocol"] = "Unknown"

        packet_list.append(packet_dict)

    return packet_list
