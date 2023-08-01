import io

import matplotlib.pyplot as plt
import networkx as nx


async def plot_connections(mac_data):
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes to the graph with MAC addresses as labels
    for mac_address, data in mac_data.items():
        G.add_node(mac_address, mac_address=mac_address, vendor=data["vendor"])

    # Add edges to the graph
    for mac_address, data in mac_data.items():
        print("data",data,mac_address)
        for connected_mac in data["devices"]:
            G.add_edge(mac_address, connected_mac)

    # Create the plot
    plt.figure(figsize=(12, 8))

    # Position the nodes using the spring_layout algorithm with increased k value
    pos = nx.spring_layout(G, seed=42, k=0.9)  # You can adjust the value of k to increase/decrease the distance

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color="skyblue", alpha=0.8)

    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color="gray", alpha=0.6)

    # Draw node labels (MAC addresses)
    labels = nx.get_node_attributes(G, "mac_address")
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=7.5, font_weight="bold")

    # Draw edge labels (optional)
    edge_labels = {(a, b): b for a, b in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    # Remove axis
    plt.axis("off")

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Clear the plot to free resources
    plt.clf()

    return buffer
