"""Greedy example colouring (order: B, A, C, D)."""
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
import shared_code

# Main function
# Define the graph.
G = shared_code.create_graph(4, shared_code.example_edges)

# Colouring
colouring = {'A': 1, 'B': 0, 'C': 2, 'D': 1}
output_colouring = shared_code.numerical_to_colours(colouring)

# Labels of node names.
labels = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D'}

# Create figure.
shared_code.output_v_one(
    G, shared_code.example_pos, output_colouring, labels,
    "..\Figures\Example-Greedy-Colouring-End.png")
