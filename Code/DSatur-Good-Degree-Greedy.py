# Imports
import shared_code

# Run everything.
# Create the graph.
G = shared_code.create_graph(8, shared_code.dsatur_good_edges)

# Colouring
colouring = {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 2, 'F': 0, 'G': 1, 'H': 1}
output_colouring = shared_code.numerical_to_colours(colouring)

# Labels to represent colouring order.
labels = {'A': 1, 'B': 5, 'C': 6, 'D': 3, 'E': 4, 'F': 2, 'G': 7, 'H': 8}

# Create figure.
shared_code.output_v_one(
    G, shared_code.dsatur_pos, output_colouring, labels,
    "..\Figures\DSatur-Good-Degree-Greedy.png")
