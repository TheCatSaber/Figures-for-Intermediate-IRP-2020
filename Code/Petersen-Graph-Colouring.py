"""Colouring of a Petersen graph."""
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
G = shared_code.create_graph(5, shared_code.petersen_edges)

# Colouring
colouring = {'A': 0, 'B': 1,'C': 1, 'D': 2, 'E': 2, 'F': 1, 'G': 0, 'H': 2,
             'I': 1, 'J': 0}
output_colouring = shared_code.numerical_to_colours(colouring)

# Create figure.
shared_code.output_v_three(
    G, shared_code.petersen_pos(list(G)), output_colouring,
    "..\Figures\Petersen-Graph-Colouring.png")
