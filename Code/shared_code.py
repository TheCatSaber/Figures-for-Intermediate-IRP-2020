"""Shared code for the other files in this folder."""
# Copyright (C) 2020 TheCatSaber

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Imports
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


# Constants
OUTPUT_COLOURS = ["blue", "red", "green", "magenta"]


# Variables
bipartite_edges = [
    ('A', 'F'), ('A', 'G'), ('A', 'H'), ('B', 'E'), ('B', 'G'), ('B', 'H'),
    ('C', 'E'), ('C', 'F'), ('C', 'H'), ('D', 'E'), ('D', 'F'), ('D', 'G')
]

bipartite_pos = {'A': (-1, 0), 'B': (-1, -1), 'C': (-1, -2), 'D': (-1, -3),
                 'E': (1, 0), 'F': (1, -1), 'G': (1, -2), 'H': (1, -3)}

dsatur_edges = [
    ('A', 'B'), ('A', 'C'), ('A', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G'),
    ('F', 'H')
]

dsatur_pos = {
    'A': (-1.5, 0), 'B': (-np.sqrt(2)/2-1.5, np.sqrt(2)/2),
    'C': (-np.sqrt(2)/2-1.5, -np.sqrt(2)/2), 'D': (-0.5, 0), 'E': (0.5, 0),
    'F': (1.5, 0), 'G': (np.sqrt(2)/2+1.5, np.sqrt(2)/2),
    'H': (np.sqrt(2)/2+1.5, -np.sqrt(2)/2)
}

example_edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D')]

example_pos = {'A': (-1, 0), 'B': (0, -1), 'C': (0, 0), 'D': (1, 0)}

degree_importance_edges = [
    ('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'C'),('C', 'D'),
    ('D', 'E')
]

degree_importance_pos = {
    'A': (0, 0), 'B': (-1, 0), 'C': (-np.sqrt(2)/2, -np.sqrt(2)/2),
    'D': (np.sqrt(2)/2, -np.sqrt(2)/2), 'E': (1, 0)
}

petersen_edges = [
    ('A', 'C'), ('A', 'D'), ('A', 'F'), ('B', 'D'), ('B', 'E'), ('B', 'G'),
    ('C', 'E'), ('C', 'H'), ('D', 'I'), ('E', 'J'), ('F', 'G'), ('G', 'H'),
    ('H', 'I'), ('I', 'J'), ('J', 'F')
]

def petersen_pos(vertices):
    """Return dict of positions for Petersen graph.

    vertices -- vertices of Petersen graph (10 element list).
    """
    pi = np.pi
    # Angles starts at top of a circle,
    # then progresses around in a clockwise direction by
    # 2/5*pi each times (108 degrees).
    angles = [pi/2, pi/10, 17*pi/10, 13*pi/10, 9*pi/10]

    inside_vertices = {vertices[counter]: (np.cos(angles[counter]), np.sin(angles[counter])) for counter in range(5)}
    outside_vertices = {vertices[counter+5]: (1.75*np.cos(angles[counter]), 1.75*np.sin(angles[counter])) for counter in range(5)}

    # Return all of the vertices
    all_vertices = {}
    for key, value in inside_vertices.items():
        all_vertices[key] = value
    for key, value in outside_vertices.items():
        all_vertices[key] = value
    return all_vertices


# Functions
def numerical_to_colours(colouring):
    """Convert numerical colouring to actual colours."""
    output_colouring = []
    for vertex, colour in colouring.items():
        # Don't worry about more colours than in OUTPUT_COLOURS
        # since number of colours needed in all code here is known.
        output_colouring.append(OUTPUT_COLOURS[colour])
    return output_colouring

def create_graph(size, edges):
    """Return networkx.Graph() object with size vertices and
    edges edges.
    
    The vertices will be unicode characters starting at 'A'.
    size -- number of vertices in graph.
    edges -- list of tuples of edges for the graph.
    """
    G = nx.Graph()
    G.add_nodes_from([chr(i) for i in range(65, 65+size)])
    G.add_edges_from(edges)
    return G

def output_v_zero(G, pos, output_colouring, labels, save_as):
    """Draw, save and show G with nx.draw_networkx.
    
    pos -- positions of vertices (dict).
    output_colouring -- colours for the vertices of G (dict).
    labels -- labels for vertices of G (dict).
    save_as -- file name to save the figure as.

    Other kwargs used for nx.draw_networkx:
    linewidths=1.75
    edgecolors="black"
    width=2
    font_color="white"
    font_weight="heavy"
    """
    nx.draw_networkx(G, pos=pos, node_color=output_colouring, linewidths=1.75,
                     edgecolors="black", width=2, labels=labels,
                     font_color="white", font_weight="heavy")

    # Equal axes (source: https://stackoverflow.com/questions/17990845).
    plt.gca().set_aspect('equal', adjustable='box')

    plt.savefig(save_as)
    plt.show()

def output_v_one(G, pos, output_colouring, labels, save_as):
    """Draw, save and show G with nx.draw_networkx.
    
    pos -- positions of vertices (dict).
    output_colouring -- colours for the vertices of G (dict).
    labels -- labels for vertices of G (dict).
    save_as -- file name to save the figure as.

    Other kwargs used for nx.draw_networkx:
    linewidths=1.75
    edgecolors="black"
    width=2
    font_color="white"
    font_weight="heavy"
    node_size=600
    font_size=20
    """
    nx.draw_networkx(G, pos=pos, node_color=output_colouring,
                     linewidths=1.75, edgecolors="black", width=2,
                     labels=labels, font_color="white", font_weight="heavy",
                     node_size=600, font_size=20)

    plt.savefig(save_as)
    plt.show()

def output_v_two(G, pos, labels, save_as):
    """Draw, save and show G with nx.draw_networkx.
    
    pos -- positions of vertices (dict).
    labels -- labels for vertices of G (dict).
    save_as -- file name to save the figure as.

    Other kwargs used for nx.draw_networkx:
    node_color="white"
    linewidths=1.75
    edgecolors="black"
    width=2
    font_color="black"
    font_weight="medium"
    node_size=600
    font_size=20
    """
    nx.draw_networkx(G, pos=pos, node_color="white",
                     linewidths=1.75, edgecolors="black", width=2,
                     labels=labels, font_color="black", font_weight="medium",
                     node_size=600, font_size=20)

    plt.savefig(save_as)
    plt.show()

def output_v_three(G, pos, output_colouring, save_as):
    """Draw, save and show G with nx.draw_networkx.
    
    pos -- positions of vertices (dict).
    output_colouring -- colours for the vertices of G (dict).
    save_as -- file name to save the figure as.

    Other kwargs used for nx.draw_networkx:
    with_labels=False
    linewidths=1.75
    edgecolors="black"
    width=2
    """
    nx.draw_networkx(G, pos=pos, with_labels=False,
                     node_color=output_colouring, linewidths=1.75,
                     edgecolors="black", width=2)

    # Equal axes (source: https://stackoverflow.com/questions/17990845).
    plt.gca().set_aspect('equal', adjustable='box')

    plt.savefig(save_as)
    plt.show()
    