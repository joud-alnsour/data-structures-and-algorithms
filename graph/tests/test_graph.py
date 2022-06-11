from graph.graph import Graph


def test_add_node():
    graph = Graph()
    actual = graph.add_node("j")
    expected = graph.adjacency_list["j"]
    assert actual == expected


def test_add_edge():
    graph = Graph()
    graph.add_node("j")
    graph.add_node("o")
    graph.add_node("u")
    graph.add_edge("j", "u", 3)
    actual = graph.adjacency_list["j"]
    expected = ["u", 3]
    assert actual == expected


def test_all_nodes():
    graph = Graph()
    graph.add_node("j")
    graph.add_node("o")
    graph.add_node("u")
    graph.add_node("d")
    actual = graph.get_node()
    expected = ["j", "o", "u", "d"]
    assert actual == expected


def test_neighbors():
    graph = Graph()
    graph.add_node("j")
    graph.add_node("o")
    graph.add_node("u")
    graph.add_edge("j", "u", 3)
    actual = graph.get_neighbor("u")
    expected = ["j", 3]
    assert actual == expected




def test_size():
    graph = Graph()
    graph.add_node("j")
    graph.add_node("o")
    graph.add_node("u")
    graph.add_node("d")
    actual = graph.size()
    expected = 4
    assert actual == expected


def test_ones():
    graph = Graph()
    graph.add_node("j")
    actual = graph.adjacency_list
    expected = {"j": []}
    assert actual == expected


def test_empty():
    graph = Graph()
    actual = graph.size()
    expected = None
    assert actual == expected