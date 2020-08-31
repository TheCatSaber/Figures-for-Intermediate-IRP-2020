# Imports
import shared_code

# Main function
# Define the graph.
G = shared_code.create_graph(4, shared_code.example_edges)

# Colouring
colouring = {'A': 2, 'B': 0, 'C': 1, 'D': 2}
output_colouring = shared_code.numerical_to_colours(colouring)

# Labels of node names.
labels = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D'}

# Create figure.
shared_code.output_v_one(
    G, shared_code.example_pos, output_colouring, labels,
    "..\Figures\Example-DSatur-Colouring-End.png")
