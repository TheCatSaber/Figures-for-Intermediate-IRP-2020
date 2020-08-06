#Imports
import networkx as nx
import matplotlib.pyplot as plt


#Constants
OUTPUT_COLOURS = ["blue", "red", "green"]


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
G.add_nodes_from([chr(i) for i in range(65, 69)])
edges = edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
G.add_edges_from(edges)

#Define the colouring
colouring = {'A': 1, 'B': 0, 'C': 2, 'D': 1}
#Convert to colours
output_colouring = numerical_to_colours(colouring)

#Define the positions of the vertices

vertices = list(G.nodes())

pos = {'A': (-1, 0), 'B': (-1, -0.5), 'C': (1, 0), 'D': (1, -0.5)}

#Labels of node name

labels = {vertex: vertex for vertex in G.nodes()}

#Draw the graph
nx.draw_networkx(G, pos=pos, with_labels=True, node_color=output_colouring, linewidths=1.75, edgecolors="black", width=2, labels=labels, font_color="white", font_weight="heavy")
plt.savefig("Example-Greedy-Colouring-End.png")
plt.show()