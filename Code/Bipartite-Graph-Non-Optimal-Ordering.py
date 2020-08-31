# Imports
import shared_code


# Run everything.
# Create the graph.
G = shared_code.create_graph(8, shared_code.bipartite_edges)

# Colouring
colouring = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 0, 'F': 1, 'G': 2, 'H': 3}
output_colouring = shared_code.numerical_to_colours(colouring)

# Labels to represent colouring order.
labels = {'A': 1, 'B': 3, 'C': 5, 'D': 7, 'E': 2, 'F': 4, 'G': 6, 'H': 8}

# Create figure.
shared_code.output_v_zero(
    G, shared_code.bipartite_pos, output_colouring, labels,
    "..\Figures\Bipartite-Graph-Non-Optimal-Ordering.png")
