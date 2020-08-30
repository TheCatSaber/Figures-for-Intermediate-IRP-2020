#Imports
import networkx as nx
import matplotlib.pyplot as plt


#Constants
OUTPUT_COLOURS = ["blue", "red"]


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
edges = [('A', 'F'), ('A', 'G'), ('A', 'H'), ('B', 'E'), ('B', 'G'), ('B', 'H'), ('C', 'E'), ('C', 'F'), ('C', 'H'), (
'D', 'E'), ('D', 'F'), ('D', 'G')]
G.add_edges_from(edges)

#Define the colouring
colouring = {'A': 0, 'B': 0,'C': 0, 'D': 0, 'E': 1, 'F': 1, 'G': 1, 'H': 1}
#Convert to colours
output_colouring = numerical_to_colours(colouring)

#Define the positions of the vertices

vertices = list(G.nodes())

pos = {}

for counter in range(len(vertices)):
    if counter < 4:
        pos[vertices[counter]] = (-1, -counter)
    else:
        pos[vertices[counter]] = (1, -(counter - 4))

#Labels to represent colouring order

labels = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}

#Draw the graph
nx.draw_networkx(G, pos=pos, with_labels=True, node_color=output_colouring, linewidths=1.75, edgecolors="black", width=2, labels=labels, font_color="white", font_weight="heavy")
#https://stackoverflow.com/questions/17990845/how-to-equalize-the-scales-of-x-axis-and-y-axis-in-python-matplotlib
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig("../Figures/Bipartite-Graphs-Optimal-Ordering.png")
plt.show()
