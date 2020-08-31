"""Show why order is important (good ordering)."""
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
G = shared_code.create_graph(5, shared_code.degree_importance_edges)

# Colouring
colouring = {'A': 0, 'B': 2, 'C': 1, 'D': 2, 'E': 1}
output_colouring = shared_code.numerical_to_colours(colouring)

# Labels to represent colouring order.
labels = {'A': 1, 'B': 4, 'C': 2, 'D': 3, 'E': 5}

# Create figure.
shared_code.output_v_one(
    G, shared_code.degree_importance_pos, output_colouring, labels,
    "..\Figures\Importance-Of-Degree-Good-Ordering.png")
