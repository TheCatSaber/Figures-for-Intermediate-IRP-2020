"""Show non-optimal ordering for a bipartite graph."""
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
G = shared_code.create_graph(8, shared_code.bipartite_edges)

# Colouring
colouring = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 0, 'F': 1, 'G': 2, 'H': 3}
output_colouring = shared_code.numerical_to_colours(colouring)

# Labels to represent colouring order.
labels = {'A': 1, 'B': 3, 'C': 5, 'D': 7, 'E': 2, 'F': 4, 'G': 6, 'H': 8}

# Create figure.
shared_code.output_v_zero(
    G, shared_code.bipartite_pos, output_colouring, labels,
    "..\Figures\Bipartite-Graph-Non-Optimal-Ordering.png")
