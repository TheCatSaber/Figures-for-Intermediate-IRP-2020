#Imports
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


#Constants
OUTPUT_COLOURS = ["blue", "red", "green", "magenta"]


#Functions
def numerical_to_colours(colouring):
    output_colouring = []
    for vertex, colour in colouring.items():
        try:
            output_colouring.append(OUTPUT_COLOURS[colour])
        except IndexError:
            raise IndexError
    return output_colouring


#Define the graph
G = nx.Graph()
G.add_nodes_from([chr(i) for i in range(65, 70)])
edges = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'C'), ('C', 'D'), ('D', 'E')]
G.add_edges_from(edges)

#Define the colouring
colouring = {'A': 3, 'B': 0, 'C': 1, 'D': 2, 'E': 0}
#Convert to colours
output_colouring = numerical_to_colours(colouring)

#Define the positions of the vertices

pos = {'A': (0, 0), 'B': (-1, 0), 'C': (-np.sqrt(2)/2, -np.sqrt(2)/2), 'D': (np.sqrt(2)/2, -np.sqrt(2)/2), 'E': (1, 0)}

#Labels to represent colouring order

labels = {'A': 5, 'B': 1, 'C': 3, 'D': 4, 'E': 2}

#Draw the graph
nx.draw_networkx(G, pos=pos, with_labels=True, node_color=output_colouring, linewidths=1.75, edgecolors="black", width=2, labels=labels, font_color="white", font_weight="heavy", node_size=600, font_size=20)
plt.savefig("Importance-Of-Order-Bad-Ordering.png")
plt.show()