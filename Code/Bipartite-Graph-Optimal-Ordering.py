# Imports
import shared_code


# Run everything.
# Create the graph.
G = shared_code.create_graph(8, shared_code.bipartite_edges)

# Colouring
colouring = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 1, 'F': 1, 'G': 1, 'H': 1}
output_colouring = shared_code.numerical_to_colours(colouring)

# Labels to represent colouring order.
labels = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}

# Create figure.
shared_code.output_v_zero(
    G, shared_code.bipartite_pos, output_colouring, labels,
    "..\Figures\Bipartite-Graph-Optimal-Ordering.png")
