class Graph:
    def __init__(self):
        self.adjacency_list = {}
        # key will be the node, value adj node with a value of the edge

    def add_node(self, value):
        v = Vertex(value)
        # Add Value to adjacency list
        # iterate through adjacency list checking for
        if v in self.adjacency_list:
            error = print("Vertex already exists")
            return error
        else:
            new_node = self.adjacency_list[v.value] = []
            return new_node

        # Arguments: value
        # Returns: The added node
        # Add a node to the graph or add to adj list

    def add_edge(self, v1, v2, edge):
        if v1 not in self.adjacency_list or v2 not in self.adjacency_list:
            error = print("Both nodes need to be in the list")
            return error
        else:
            edge1 = Edge(v2, edge)
            edge2 = Edge(v1, edge)
            if v1 == v2:
                self.adjacency_list[v1].append(edge1.vertex)
                self.adjacency_list[v1].append(edge1.weight)
            else:
                self.adjacency_list[v1].append(edge1.vertex)
                self.adjacency_list[v1].append(edge1.weight)
                self.adjacency_list[v2].append(edge2.vertex)
                self.adjacency_list[v2].append(edge2.weight)

        # Arguments: 2 nodes to be connected by the edge, weight (optional)
        # Returns: nothing
        # Adds a new edge between two nodes in the graph
        # If specified, assign a weight to the edge
        # Both nodes should already be in the Graph

    def get_node(self):
        all_nodes = []
        for node in self.adjacency_list:
            all_nodes.append(node)

        return all_nodes
        # Arguments: none
        # Returns all nodes in graph as a collection (set, list, or similar)

    def get_neighbor(self, v):
        neighbors = self.adjacency_list[v]
        if len(neighbors) == 0:
            return "No adjacent vertices"
        else:
            return neighbors

        # Arguments: node
        # Returns a collection of edges connected to the given node
        # Include the weight of connection in returned collection

    def size(self):
        if len(self.adjacency_list) == 0:
            return None
        else:
            return len(self.adjacency_list)

        # Arguments: none
        # Returns the total number of nodes in the graph


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight


if __name__ == "__main__":
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")

    graph.add_edge("a", "c", 3)
    print(graph.size())
    print(graph.get_neighbor("c"))
    print(graph.get_node())




