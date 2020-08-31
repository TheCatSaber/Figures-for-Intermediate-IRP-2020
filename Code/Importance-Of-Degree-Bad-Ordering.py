# Imports
import shared_code

# Main function
# Define the graph.
G = shared_code.create_graph(5, shared_code.degree_importance_edges)

# Colouring
colouring = {'A': 3, 'B': 0, 'C': 1, 'D': 2, 'E': 0}
output_colouring = shared_code.numerical_to_colours(colouring)

# Labels to represent colouring order.
labels = {'A': 5, 'B': 1, 'C': 3, 'D': 4, 'E': 2}

# Create figure.
shared_code.output_v_one(
    G, shared_code.degree_importance_pos, output_colouring, labels,
    "..\Figures\Importance-Of-Degree-Bad-Ordering.png")
