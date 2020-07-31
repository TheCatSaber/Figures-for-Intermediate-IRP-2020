#Imports
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


#Constants
OUTPUT_COLOURS = ["blue", "lime", "red"]


#Functions
def numerical_to_colours(colouring):
    output_colouring = []
    for vertex, colour in colouring.items():
        output_colouring.append(OUTPUT_COLOURS[colour])
    return output_colouring

#Define the graph
G = nx.Graph()
G.add_nodes_from([chr(i) for i in range(65, 75)])
edges = [('A', 'C'), ('A', 'D'), ('A', 'F'), ('B', 'D'), ('B', 'E'), ('B', 'G'), ('C', 'E'), ('C', 'H'), ('D', 'I'), ('E', 'J'), ('F', 'G'), ('G', 'H'), ('H', 'I'), ('I', 'J'), ('J', 'F')]
G.add_edges_from(edges)

#Define the colouring
colouring = {'A': 0, 'B': 1,'C': 1, 'D': 2, 'E': 2, 'F': 1, 'G': 0, 'H': 2, 'I': 1, 'J': 0}
#Convert to colours
output_colouring = numerical_to_colours(colouring)

#Define the positions of the vertices
angles = [np.pi/2, np.pi/10, 17*np.pi/10, 13*np.pi/10, 9*np.pi/10]

vertices = list(G.nodes())

pos = {}

for i in range(0,10):
    if i < 5:
        pos[vertices[i]] = (np.cos(angles[i]), np.sin(angles[i]))
    else:
        pos[vertices[i]] = (1.75*np.cos(angles[i-5]), 1.75*np.sin(angles[i-5]))

#Draw the graph
nx.draw_networkx(G, pos=pos, with_labels=False, node_color=output_colouring, linewidths=1.75, edgecolors="black", width=2)
#https://stackoverflow.com/questions/17990845/how-to-equalize-the-scales-of-x-axis-and-y-axis-in-python-matplotlib
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig("Petersen-Graph-Colouring.png")
plt.show()
