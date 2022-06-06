class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        pre_list = []

        def walk(root):
            if root is None:
                return
            pre_list.append(root.value)
            walk(root.left)
            walk(root.right)

        walk(self.root)
        return pre_list

    def in_order(self):
        in_list = []

        def walk(root):
            if root is None:
                return

            walk(root.left)
            in_list.append(root.value)
            walk(root.right)

        walk(self.root)
        return in_list

    def post_order(self):
        post_list = []

        def walk(root):
            if root is None:
                return

            walk(root.left)
            walk(root.right)
            post_list.append(root.value)

        walk(self.root)
        return post_list

class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]
    def hash(self, key):
        # Arguments: key
        # Returns: Index in the collection for that key
        sum = 0
        for char in key:
            sum += ord(char)
        primed = sum * 521
        return  primed % self.size
    def set(self, key, value):
        # Arguments: key, value
        # Returns: nothing
        # This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        # Should a given key already exist, replace its value from the value argument given to this method.
       index = self.hash(key)
       key_found = False

       for i, record in enumerate(self.buckets[index]):
           if len(record) == 2 and record[0] == key:
               self.buckets[index][i] = (key, value)
               key_found = True
               break

       if not key_found:
           self.buckets[index].append((key,value))

    def get(self, key):
        # Arguments: key
        # Returns: Value associated with that key in the table
        index = self.hash(key)
        for record in self.buckets[index]:
            if record[0] == key:
                return record[1]
    def contains(self, key):
        # Arguments: key
        # Returns: Boolean, indicating if the key exists in the table already.
        index = self.hash(key)
        for record in self.buckets[index]:
            if record[0] == key:
                return True
        return False
    def keys(self):
        # Returns: Collection of keys
        for record in self.buckets:
            return print(record)
        # return print(self.buckets)
 
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

if __name__ == "__main__":
    tree1 = BinaryTree()
    tree1.root = Node(150)
    tree1.root.right = Node(250)
    tree1.root.left = Node(100)
    tree1.root.left.left = Node(75)
    tree1.root.right.left = Node(200)

    tree2 = BinaryTree()
    tree2.root = Node(42)
    tree2.root.right = Node(600)
    tree2.root.left = Node(100)
    tree2.root.left.left = Node(18)
    tree2.root.right.left = Node(200)

    print(tree_intersection(tree1, tree2))



