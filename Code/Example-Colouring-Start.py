#Imports
import networkx as nx
import matplotlib.pyplot as plt


#Define the graph
G = nx.Graph()
G.add_nodes_from([chr(i) for i in range(65, 69)])
edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
G.add_edges_from(edges)

#Define the positions of the vertices

pos = {'A': (-1, 0), 'B': (0, -1), 'C': (0, 0), 'D': (1, 0)}

#Labels of node names

labels = {vertex: vertex for vertex in G.nodes()}

#Draw the graph
nx.draw_networkx(G, pos=pos, with_labels=True, node_color="white", linewidths=1.75, edgecolors="black", width=2, labels=labels, font_color="black", font_weight="medium", node_size=600, font_size=20)
plt.savefig("../Figures/Example-Colouring-Start.png")
plt.show()