# Code Challenge: Class 15
# Trees
Node Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

Binary Tree Create a Binary Tree class Define a method for each of the depth first traversals: pre order in order post order which returns an array of the values, ordered appropriately.
- Implement Binary Tree class and its traversal methods

Binary Search Tree Create a Binary Search Tree class This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods: Add Arguments: value Return: nothing Adds a new node with that value in the correct location in the binary search tree. Contains Argument: value Returns: boolean indicating whether or not the value is in the tree at least once.
- implement BST class and its add and contains method

## Challenge
Create a node, binary tree, and binary search tree class and perform the tasks above.


## Approach & Efficiency
I took a TDD approach with this because that would be the optimal way when writing code. Big O: Binary Tree: Space:O(w) Time:O(n) Binary Search Tree: Space:O(1) Time:O(h)


## API
pre_order - returns a list of the values in a Binary Tree via a pre order traversal. in_order - returns a list of the values in a Binary Tree via an in order traversal. post_order - returns a list of the values in a Binary Tree via a post order traversal.

add - Adds a value to a binary search tree contains - Returns a boolean indicating whether or not the given value is in the tree at least once.

- [x] Create (Node class,BinaryTree class and BinarySearchTree class).
- [x] Create (pre_order method ,in_order method, post_order method,Add method and Contains method).

# Code Challenge: Class 16
# Trees-max
Binary Tree Create a Binary Tree class Define a method that finds the max value in a Binary Tree
## Challenge Summary
The code challenge was to create a method that finds the max value in a binary tree.
## Whiteboard Process
![pic](/trees/maxTree.jpg)
## Approach & Efficiency
- Define a max value and compare each value to each node in the tree. Traverse each node in the tree and compare to a max value.<br>
Big O<br>
time: O(n)<br>
space: O(1)

## Solution
***Code***
```
 def max_value(self):
        # going to use the post order left > right > root to find the max value
        if self.root == None:
            raise Exception("Sorry this Tree is currently empty")

        # current_max_value = 0
        z = {'max_value': 0}
        def walk(node, z):
            if node:
                walk(node.left, z)
                walk(node.right, z)
                if node.value > z["max_value"]:
                    z['max_value'] = node.value
        walk(self.root, z)
        return z['max_value']
```
***Test***
```
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
``` 

