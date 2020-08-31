"""Start of example colouring."""
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

# Labels of node names.
labels = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D'}

# Create figure.
shared_code.output_v_two(
    G, shared_code.example_pos, labels,
    "..\Figures\Example-Colouring-Start.png")
