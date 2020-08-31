# Imports
import shared_code

# Main function
# Define the graph.
G = shared_code.create_graph(4, shared_code.example_edges)

# Labels of node names.
labels = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D'}

# Create figure.
shared_code.output_v_one(
    G, shared_code.example_pos, {vertex: "white" for vertex in G}, labels,
    "..\Figures\Example-Colouring-Start.png")
