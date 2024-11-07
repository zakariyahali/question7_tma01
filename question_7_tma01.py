import networkx as nx
import matplotlib.pyplot as plt

# Create directed graph
G = nx.DiGraph()

# Add nodes and edges with capacities and flows
edges = [
    ('S', 'A', 12, 7), ('S', 'B', 15, 10),
    ('A', 'C', 7, 7), ('A', 'D', 4, 0),
    ('B', 'D', 4, 4), ('B', 'E', 8, 6),
    ('C', 'F', 9, 7), ('C', 'G_in', 2, 0),
    ('D', 'G_in', 10, 4), ('E', 'H', 6, 6),
    ('F', 'I', 9, 7), ('G_out', 'I', 7, 0),
    ('G_out', 'J', 8, 0), ('H', 'J', 8, 6),
    ('I', 'T', 15, 7), ('J', 'T', 10, 10)
]

# Add nodes and capacity constraint for G
G.add_nodes_from(['G_in', 'G_out'])
G.add_edge('G_in', 'G_out', capacity=9, flow=4)

# Add edges to the graph
for u, v, capacity, flow in edges:
    G.add_edge(u, v, capacity=capacity, flow=flow)

# Positions for nodes
pos = {
    'S': (0, 2), 'A': (1, 3), 'B': (1, 1),
    'C': (2, 3.5), 'D': (2, 2), 'E': (2, 0.5),
    'F': (3, 3.5), 'G_in': (3, 2.5), 'G_out': (4, 2.5),
    'H': (3, 0.5), 'I': (5, 3.5), 'J': (5, 1),
    'T': (6, 2)
}

# Draw the graph with capacities and flows
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)

# Draw edge labels for capacity and flow
edge_labels = {(u, v): f"{flow}/{capacity}" for u, v, capacity, flow in edges}
edge_labels[('G_in', 'G_out')] = "4/9"  # Manually add G split node's label
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

# Highlight saturated edges in red
saturated_edges = [(u, v) for u, v, capacity, flow in edges if flow == capacity]
nx.draw_networkx_edges(G, pos, edgelist=saturated_edges, edge_color='red', width=2)

# Highlight minimum cut edges in green for Cut 1
cut1_edges = [('A', 'C'), ('F', 'I'), ('E', 'H')]
nx.draw_networkx_edges(G, pos, edgelist=cut1_edges, edge_color='green', width=2, style='dashed')

# Highlight minimum cut edges in purple for Cut 2
cut2_edges = [('S', 'A'), ('S', 'B'), ('G_in', 'G_out')]
nx.draw_networkx_edges(G, pos, edgelist=cut2_edges, edge_color='purple', width=2, style='dashed')

# Display the plot
plt.title("Network Flow Diagram with Saturated Edges and Minimum Cuts")
plt.show()
