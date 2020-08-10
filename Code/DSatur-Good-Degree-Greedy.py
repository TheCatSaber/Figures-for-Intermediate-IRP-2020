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
G.add_nodes_from([chr(i) for i in range(65, 73)])
edges = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G'), ('F', 'H')]
G.add_edges_from(edges)

#Define the colouring
colouring = {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 2, 'F': 0, 'G': 1, 'H': 1}
#Convert to colours
output_colouring = numerical_to_colours(colouring)

#Define the positions of the vertices

pos = {'A': (-1.5, 0), 'B': (-np.sqrt(2)/2-1.5, np.sqrt(2)/2), 'C': (-np.sqrt(2)/2-1.5, -np.sqrt(2)/2), 'D': (-0.5, 0), 'E': (0.5, 0), 'F': (1.5, 0), 'G': (np.sqrt(2)/2+1.5, np.sqrt(2)/2), 'H': (np.sqrt(2)/2+1.5, -np.sqrt(2)/2)}

#Labels to represent colouring order

labels = {'A': 1, 'B': 5, 'C': 6, 'D': 3, 'E': 4, 'F': 2, 'G': 7, 'H': 8}

#Draw the graph
nx.draw_networkx(G, pos=pos, with_labels=True, node_color=output_colouring, linewidths=1.75, edgecolors="black", width=2, labels=labels, font_color="white", font_weight="heavy", node_size=600, font_size=20)
plt.savefig("DSatur-Good-Degree-Greedy.png")
plt.show()