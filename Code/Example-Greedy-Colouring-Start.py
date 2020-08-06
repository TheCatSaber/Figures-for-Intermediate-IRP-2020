#Imports
import networkx as nx
import matplotlib.pyplot as plt


#Define the graph
G = nx.Graph()
G.add_nodes_from([chr(i) for i in range(65, 69)])
edges = edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
G.add_edges_from(edges)

#Define the positions of the vertices

vertices = list(G.nodes())

pos = {'A': (-1, 0), 'B': (-1, -0.5), 'C': (1, 0), 'D': (1, -0.5)}

#Labels of node name

labels = {vertex: vertex for vertex in G.nodes()}

#Draw the graph
nx.draw_networkx(G, pos=pos, with_labels=True, node_color="white", linewidths=1.75, edgecolors="black", width=2, labels=labels, font_color="black", font_weight="medium")
plt.savefig("Example-Greedy-Colouring-Start.png")
plt.show()