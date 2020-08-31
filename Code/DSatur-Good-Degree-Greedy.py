"""Demonstration of why DSaur is good (Degree Greedy version)."""
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

# Run everything.
# Create the graph.
G = shared_code.create_graph(8, shared_code.dsatur_edges)

# Colouring
colouring = {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 2, 'F': 0, 'G': 1, 'H': 1}
output_colouring = shared_code.numerical_to_colours(colouring)

# Labels to represent colouring order.
labels = {'A': 1, 'B': 5, 'C': 6, 'D': 3, 'E': 4, 'F': 2, 'G': 7, 'H': 8}

# Create figure.
shared_code.output_v_one(
    G, shared_code.dsatur_pos, output_colouring, labels,
    "..\Figures\DSatur-Good-Degree-Greedy.png")
