class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        node1 = Vertex(value)
        
        if node1 in self.adjacency_list:
            error = print("Vertex already exists")
            return error
        else:
            new_node = self.adjacency_list[node1.value] = []
            return new_node

    def add_edge(self, egde1, egde2, edge):
        if egde1 not in self.adjacency_list or egde2 not in self.adjacency_list:
            error = print("Both nodes need to be in the list")
            return error
        else:
            edge1 = Edge(egde2, edge)
            edge2 = Edge(egde1, edge)
            if egde1 == egde2:
                self.adjacency_list[egde1].append(edge1.vertex)
                self.adjacency_list[egde1].append(edge1.weight)
            else:
                self.adjacency_list[egde1].append(edge1.vertex)
                self.adjacency_list[egde1].append(edge1.weight)
                self.adjacency_list[egde2].append(edge2.vertex)
                self.adjacency_list[egde2].append(edge2.weight)


    def get_node(self):
        nodes = []
        for node in self.adjacency_list:
            nodes.append(node)

        return nodes
     

    def get_neighbor(self, vertices):
        neighbors = self.adjacency_list[vertices]
        if len(neighbors) == 0:
            return "No adjacent vertices"
        else:
            return neighbors

       

    def size(self):
        if len(self.adjacency_list) == 0:
            return None
        else:
            return len(self.adjacency_list)

     


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight


if __name__ == "__main__":
    graph = Graph()
    graph.add_node("j")
    graph.add_node("o")
    graph.add_node("u")

    graph.add_edge("j", "u", 3)
    print(graph.size())
    print(graph.get_neighbor("u"))
    print(graph.get_node())




