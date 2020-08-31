# Imports
import shared_code

# Main function
# Define the graph.
G = shared_code.create_graph(5, shared_code.petersen_edges)

# Colouring
colouring = {'A': 0, 'B': 1,'C': 1, 'D': 2, 'E': 2, 'F': 1, 'G': 0, 'H': 2,
             'I': 1, 'J': 0}
output_colouring = shared_code.numerical_to_colours(colouring)

# Create figure.
shared_code.output_v_three(
    G, shared_code.petersen_pos(list(G)), output_colouring,
    "..\Figures\Petersen-Graph-Colouring.png")
