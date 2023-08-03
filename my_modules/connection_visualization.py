# # # # import io
# # # #
# # # # import matplotlib.pyplot as plt
# # # # import networkx as nx
# # # #
# # # #
# # # # async def plot_connections(mac_data):
# # # #     # Create a directed graph
# # # #     G = nx.DiGraph()
# # # #
# # # #     # Add nodes to the graph with MAC addresses as labels
# # # #     for mac_address, data in mac_data.items():
# # # #         G.add_node(mac_address, mac_address=mac_address, vendor=data["vendor"])
# # # #
# # # #     # Add edges to the graph
# # # #     for mac_address, data in mac_data.items():
# # # #         print("data",data,mac_address)
# # # #         for connected_mac in data["devices"]:
# # # #             G.add_edge(mac_address, connected_mac)
# # # #
# # # #     # Create the plot
# # # #     plt.figure(figsize=(12, 8))
# # # #
# # # #     # Position the nodes using the spring_layout algorithm with increased k value
# # # #     pos = nx.spring_layout(G, seed=42, k=0.9)  # You can adjust the value of k to increase/decrease the distance
# # # #
# # # #     # Draw nodes
# # # #     nx.draw_networkx_nodes(G, pos, node_size=2000, node_color="skyblue", alpha=0.8)
# # # #
# # # #     # Draw edges
# # # #     nx.draw_networkx_edges(G, pos, edge_color="gray", alpha=0.6)
# # # #
# # # #     # Draw node labels (MAC addresses)
# # # #     labels = nx.get_node_attributes(G, "mac_address")
# # # #     nx.draw_networkx_labels(G, pos, labels=labels, font_size=7.5, font_weight="bold")
# # # #
# # # #     # Draw edge labels (optional)
# # # #     edge_labels = {(a, b): b for a, b in G.edges()}
# # # #     nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
# # # #
# # # #     # Remove axis
# # # #     plt.axis("off")
# # # #
# # # #     # Save the plot to a BytesIO object
# # # #     buffer = io.BytesIO()
# # # #     plt.savefig(buffer, format='png')
# # # #     buffer.seek(0)
# # # #
# # # #     # Clear the plot to free resources
# # # #     plt.clf()
# # # #
# # # #     return buffer
# # #


import io

import matplotlib.pyplot as plt
import networkx as nx

from tmp import find_the_router


async def plot_connections(mac_data):
    router = await find_the_router(mac_data)
    router_mac = router["router_mac_address"]
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes to the graph with MAC addresses as labels
    for mac_address, data in mac_data.items():
        G.add_node(mac_address, mac_address=mac_address)

    # Add edges to the graph
    for mac_address, data in mac_data.items():
        for connected_mac, connection_info in data["devices"].items():
            protocol_types = connection_info["protocol_type"]
            edge_label = ", ".join(protocol_types)
            if "dest_ip_address" in connection_info:
                edge_label += f"\nDst IP: {connection_info['dest_ip_address']}"

            G.add_edge(mac_address, connected_mac, label=edge_label)

    # Create the plot
    plt.figure(figsize=(12, 8))

    # Position the nodes using the spring_layout algorithm
    pos = nx.spring_layout(G, seed=42, k=0.8)
    # Draw nodes
    node_colors = ["red" if node == router_mac else "skyblue" for node in G.nodes]
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color=node_colors, alpha=0.8)

    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color="gray", alpha=0.6)

    # Draw node labels (MAC addresses and vendors)
    node_labels = {mac_address: f"{mac_address}" for mac_address, data in mac_data.items()}
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=7.5, font_weight="bold")

    # Draw edge labels (protocol types and destination IP)
    edge_labels = nx.get_edge_attributes(G, "label")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    # Remove axis
    plt.axis("off")

    # Save the plot to a buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0)
    buffer.seek(0)

    # Clear the plot to free resources
    plt.clf()

    return buffer
