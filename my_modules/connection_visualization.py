import io

import matplotlib.pyplot as plt
import networkx as nx
from PIL import Image


# mac_data = {
#     "00:0c:29:1f:f8:1a": {
#         "devices": ["ff:ff:ff:ff:ff:ff", "00:50:56:c0:00:02", "00:50:56:c0:00:02"],
#         "vendor": "VMware, Inc.",
#     },
#     "00:0c:29:69:e6:2b": {
#         "devices": ["00:0c:29:b0:8d:62", "00:0c:29:b0:8d:62", "00:50:56:c0:00:02"],
#         "vendor": "VMware, Inc.",
#     },
# }


async def plot_connections(mac_data):
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes to the graph with MAC addresses as labels
    for mac_address, data in mac_data.items():
        G.add_node(mac_address, vendor=data["vendor"], mac_address=mac_address)

    # Add edges to the graph
    for mac_address, data in mac_data.items():
        for connected_mac in data["devices"]:
            G.add_edge(mac_address, connected_mac)

    # Create the plot
    plt.figure(figsize=(12, 8))

    # Position the nodes using the spring_layout algorithm
    pos = nx.spring_layout(G, seed=42)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color="skyblue", alpha=0.8)

    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color="gray", alpha=0.6)

    # Draw node labels (MAC addresses)
    labels = nx.get_node_attributes(G, "mac_address")
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, font_weight="bold")

    # Draw edge labels (optional)
    edge_labels = {(a, b): b for a, b in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    # Remove axis
    plt.axis("off")

    # Show the plot
    plt.show()
    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    # buffer.seek(0)
    return buffer

# to converting reason is because I want to return to client this graf as picture
# async def convert_plot_to_picture(graf):
#     buffer = io.BytesIO()
#     plt.savefig(buffer, format="png", bbox_inches="tight")
#     plt.close()
#
#     # Convert the binary buffer to a PIL image
#     buffer.seek(0)
#     img = Image.open(buffer)
#
#     # Save the image as PNG file
#     png_buffer = io.BytesIO()
#     img.save(png_buffer, format="PNG")
#     buffer.close()
#
#     # Return the image as bytes
#     return png_buffer.getvalue()
