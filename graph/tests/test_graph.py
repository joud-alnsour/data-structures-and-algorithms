from graph.graph import Graph

# Write tests to prove the following functionality:

# Node can be successfully added to the graph
def test_add_node():
    graph = Graph()
    actual = graph.add_node("a")
    expected = graph.adjacency_list["a"]
    assert actual == expected


# An edge can be successfully added to the graph
def test_add_edge():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_edge("a", "c", 3)
    actual = graph.adjacency_list["a"]
    expected = ["c", 3]
    assert actual == expected


# A collection of all nodes can be properly retrieved from the graph
def test_all_nodes():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    actual = graph.get_node()
    expected = ["a", "b", "c"]
    assert actual == expected


# All appropriate neighbors can be retrieved from the graph
def test_neighbors():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_edge("a", "c", 3)
    actual = graph.get_neighbor("c")
    expected = ["a", 3]
    assert actual == expected


# Neighbors are returned with the weight between nodes included
def test_neighbors_weight():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_edge("a", "c", 3)
    actual = graph.get_neighbor("c")
    expected = ["a", 3]
    assert actual == expected


# The proper size is returned, representing the number of nodes in the graph
def test_size():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    actual = graph.size()
    expected = 3
    assert actual == expected


# A graph with only one node and edge can be properly returned
def test_ones():
    graph = Graph()
    graph.add_node("a")
    actual = graph.adjacency_list
    expected = {"a": []}
    assert actual == expected


# An empty graph properly returns null
def test_empty():
    graph = Graph()
    actual = graph.size()
    expected = None
    assert actual == expected