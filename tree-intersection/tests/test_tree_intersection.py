from tree_intersection.tree_intersection import tree_intersection, BinaryTree,Node
import pytest


@pytest.fixture
def tree_one():
    tree1 = BinaryTree()
    tree1.root = Node(2)
    return tree1


@pytest.fixture    
def tree_two():

    tree2 = BinaryTree()
    tree2.root = Node(2)
    return tree2


@pytest.fixture
def tree_three():
    tree1 = BinaryTree()
    tree1.root = Node(150)
    tree1.root.right = Node(42)
    tree1.root.left = Node(3)
    tree1.root.left.left = Node(15)
    tree1.root.right.left = Node(33)
    return tree1


@pytest.fixture    
def tree_four():

    tree2= BinaryTree()
    tree2.root = Node(150)
    tree2.root.right = Node(42)
    tree2.root.left = Node(5)
    tree2.root.left.left = Node(15)
    tree2.root.right.left = Node(20)
    return tree2


 
def test_tree_intersection_fail():
    with pytest.raises(Exception):
        tree_intersection(BinaryTree(),BinaryTree())


def test_tree_intersection3(tree_one,tree_two):
    actual = tree_intersection(tree_one,tree_two)
    expected = [2]
    assert actual == expected


def test_tree_intersection(tree_three,tree_four):

    actual = tree_intersection(tree_three,tree_four)
    expected = [150, 15, 42]
    assert actual == expected
 

 
