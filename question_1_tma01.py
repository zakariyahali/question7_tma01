import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Define the original graph G
G = nx.Graph()
# Adding edges for the simple Hamiltonian graph (triangle with internal nodes)
edges = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 0), # Hamiltonian cycle
    (0, 2), (0, 3), (1, 3), (1, 4), (2, 4) # Inner edges
]
G.add_edges_from(edges)

# Step 2: Draw the original graph G with the Hamiltonian cycle highlighted
plt.figure(figsize=(8, 6))
pos = nx.shell_layout(G)  # Arrange nodes in a shell layout

# Draw all edges in light gray
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='lightgray', font_size=12)

# Highlight the Hamiltonian cycle in red
hamiltonian_cycle_edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
nx.draw_networkx_edges(G, pos, edgelist=hamiltonian_cycle_edges, edge_color='red', width=2)

plt.title("Graph G with Hamiltonian Cycle Highlighted")
plt.show()

# Step 3: Redraw G as a hexagon with the Hamiltonian cycle on the outer edges
plt.figure(figsize=(8, 6))
# Manually position nodes in a hexagonal layout
hex_pos = {
    0: (1, 0), 1: (0.5, 0.866), 2: (-0.5, 0.866),
    3: (-1, 0), 4: (-0.5, -0.866), 5: (0.5, -0.866)
}

# Draw all edges in light gray
nx.draw(G, hex_pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='lightgray', font_size=12)

# Highlight the Hamiltonian cycle (outer hexagon) in red
nx.draw_networkx_edges(G, hex_pos, edgelist=hamiltonian_cycle_edges, edge_color='red', width=2)

# Highlight the K4 subgraph in blue
K4_edges = [(0, 2), (2, 4), (4, 1), (1, 3)]
nx.draw_networkx_edges(G, hex_pos, edgelist=K4_edges, edge_color='blue', width=2)

plt.title("Graph G in Hexagon Layout with Hamiltonian Cycle and K4 Subgraph")
plt.show()

# Step 4: Define a new graph H with the same degree sequence but not isomorphic to G
H = nx.Graph()
# Adding edges for H with the same degree sequence as G but in a different structure
H_edges = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 0), # Hamiltonian cycle
    (0, 2), (1, 3), (1, 4), (2, 4), (3, 0) # Inner edges
]
H.add_edges_from(H_edges)

# Step 5: Draw graph H as a hexagon with Hamiltonian cycle and inner edges
plt.figure(figsize=(8, 6))
# Reuse the hexagonal layout positions
nx.draw(H, hex_pos, with_labels=True, node_color='lightgreen', node_size=500, edge_color='lightgray', font_size=12)

# Highlight the Hamiltonian cycle in red
nx.draw_networkx_edges(H, hex_pos, edgelist=hamiltonian_cycle_edges, edge_color='red', width=2)

plt.title("Graph H with Same Degree Sequence as G but Not Isomorphic")
plt.show()
