import pytest
from trees.trees import Node, BinaryTree, BinarySearchTree

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