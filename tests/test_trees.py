import pytest
from trees.trees import Node, BinaryTree, BinarySearchTree, Queue

def test_binary_tree_empty():
    assert BinaryTree

def test_binary_tree_root():
    one = Node("1")
    tree = BinaryTree(one)
    assert tree.root.value == "1"

def test_binary_tree_left():
    one = Node("1")
    one.left = Node("2")
    tree = BinaryTree(one)
    assert tree.root.left.value == "2"

def test_binary_tree_right():
    one = Node("1")
    one.right = Node("3")
    tree = BinaryTree(one)
    assert tree.root.right.value == "3"

def test_binary_pre_order():
    one = Node("1")
    one.left = Node("2")
    one.right = Node("3")
    tree = BinaryTree(one)
    assert tree.pre_order() == ["1","2","3"]

def test_binary_in_order():
    one = Node("1")
    one.left = Node("2")
    one.right = Node("3")
    tree = BinaryTree(one)
    assert tree.in_order() == ["2","1","3"]

def test_binary_post_order():
    one = Node("1")
    one.left = Node("2")
    one.right = Node("3")
    tree = BinaryTree(one)
    assert tree.post_order() == ["2","3","1"]

def test_binary_search():
    bst = BinarySearchTree()
    assert isinstance(bst, BinaryTree)

def test_binary_search_empty():
    assert BinarySearchTree()

def test_binary_search_add():
    bst = BinarySearchTree()
    bst.add(1)
    assert bst.root.value == 1

def test_binary_search_contains_false():
    one = Node(1)
    one.left = Node(2)
    one.right = Node (3)
    bst = BinarySearchTree(one)
    assert bst.contains(4) == False

def test_binary_search_contains_true():
    one = Node(1)
    one.left = Node(2)
    one.right = Node (3)
    bst = BinarySearchTree(one)
    assert bst.contains(3) == True

#Max Value Test
def test_max_value():
    one = Node(1)
    three = Node(3)
    four = Node(4)
    bt = BinaryTree(one)
    one.left = four
    one.right = three
    assert one.left == bt.root.left
    assert one.right == three
    max = bt.max_value()
    assert max == 4


def test_max_right():
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    bt = BinaryTree(root)
    assert bt.max_value() == 6

def test_max_is_empty():
    bt = BinaryTree()
    with pytest.raises(Exception):
        bt.max_value()

def test_max_multiple():
    root = Node(3)
    root.left = Node(7)
    root.right = Node(2)
    root.right.right = Node (11)
    bt = BinaryTree(root)
    assert bt.max_value() == 11

def test_max_complex():
    root = Node(5)
    root.left = Node(7)
    root.right = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(13)
    bt = BinaryTree(root)
    assert bt.max_value() == 13

# tree-breadth-first Test
def test_empty_queue():
  empty_q = Queue()
  print('I am in the test')
  assert empty_q.isEmpty() == True
