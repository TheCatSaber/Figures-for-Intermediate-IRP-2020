# Imports
import shared_code

# Main function
# Define the graph.
G = shared_code.create_graph(5, shared_code.degree_importance_edges)

# Colouring
colouring = {'A': 0, 'B': 2, 'C': 1, 'D': 2, 'E': 1}
output_colouring = shared_code.numerical_to_colours(colouring)

# Labels to represent colouring order.
labels = {'A': 1, 'B': 4, 'C': 2, 'D': 3, 'E': 5}

# Create figure.
shared_code.output_v_one(
    G, shared_code.degree_importance_pos, output_colouring, labels,
    "..\Figures\Importance-Of-Degree-Good-Ordering.png")
