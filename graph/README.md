# Graphs
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

## Challenge
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

- add_node
- add_edge
- get_node
- get_neighbor
- size
## Approach & Efficiency
**The Big(O):** <br> 
time: O(1) <br>
space: O(n) because the amount of conversions grows depending on the amount of keys.


## API
- add_node
     - Arguments: value
     - Returns: The added node
     - Add a node to the graph or add to adj list

- add_edge
     - Arguments: 2 nodes to be connected by the edge, weight (optional)
     - Returns: nothing
     - Adds a new edge between two nodes in the graph
     - If specified, assign a weight to the edge
     - Both nodes should already be in the Graph

- get_node
     - Arguments: none
     - Returns all of the nodes in the graph as a collection (set, list, or similar)

- get_neighbor
     - Arguments: node
     - Returns a collection of edges connected to the given node
     - Include the weight of the connection in the returned collection

- size
     - Arguments: none
     - Returns the total number of nodes in the graph


