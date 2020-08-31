# Imports
import networkx as nx
import matplotlib.pyplot as plt


# Constants
OUTPUT_COLOURS = ["blue", "red", "green", "magenta"]


# Functions
def numerical_to_colours(colouring):
    """Convert numberical colouring to actual colours."""
    output_colouring = []
    for vertex, colour in colouring.items():
        try:
            output_colouring.append(OUTPUT_COLOURS[colour])
        except IndexError:
            raise IndexError
    return output_colouring


# Main function
# Define the graph
G = nx.Graph()
G.add_nodes_from([chr(i) for i in range(65, 73)])
edges = [('A', 'F'), ('A', 'G'), ('A', 'H'), ('B', 'E'), ('B', 'G'),
         ('B', 'H'), ('C', 'E'), ('C', 'F'), ('C', 'H'), ('D', 'E'),
         ('D', 'F'), ('D', 'G')]
G.add_edges_from(edges)

# Define the colouring
colouring = {'A': 0, 'B': 1,'C': 2, 'D': 3, 'E': 0, 'F': 1, 'G': 2, 'H': 3}

# Convert to colours
output_colouring = numerical_to_colours(colouring)

# Define the positions of the vertices
vertices = list(G)
pos = {}
for counter in range(len(vertices)):
    if counter < 4:
        pos[vertices[counter]] = (-1, -counter)
    else:
        pos[vertices[counter]] = (1, -(counter - 4))

# Labels to represent colouring order
labels = {'A': 1, 'B': 3, 'C': 5, 'D': 7, 'E': 2, 'F': 4, 'G': 6, 'H': 8}

# Draw the graph
nx.draw_networkx(G, pos=pos, with_labels=True, node_color=output_colouring,
                 linewidths=1.75, edgecolors="black", width=2, labels=labels,
                 font_color="white", font_weight="heavy")

# Save the graph
# From: https://stackoverflow.com/questions/17990845
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig("../Figures/Bipartite-Graphs-Non-Optimal-Ordering.png")
plt.show()
