# Challenge Summary:Class 32
Create a tree intersection function that takes two binary trees as parameters. Return a set of values found in both trees using your Hashmap implementation as part of your algorithm.
## Whiteboard Process
![pic](/tree-intersection/assets/intersection.jpg)
## Approach & Efficiency
Big O<br>
time:O(1)<br>
space:O(n)<br>
## Solution
 ***Code***
```
def tree_intersection(tree1,tree2):
    new = []
    if tree1.root == None or tree2.root == None:
        raise Exception ("empty tree")
    tree1 = tree1.pre_order()
    tree2 = tree2.pre_order()
    hashtable = Hashtable()
    for value in tree1:
        hashtable.set(key=str(value), value=value)
    for value in tree2:
        if hashtable.contains(str(value)):
            new.append(value)
    return new
```
***Test***  
```
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
```

- [x] done README file 
- [x] done Whiteboard
- [x] done the test 
- [x] done the code 