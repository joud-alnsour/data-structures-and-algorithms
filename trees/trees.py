class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

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


class BinarySearchTree(BinaryTree):

    def add(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node

        def walk(root, add_node):
            if root is None:
                return

            if add_node.value < root.value:
                if root.left:
                    walk(root.left, add_node)
                else:
                    root.left = add_node
            else:
                if root.right:
                    walk(root.right, add_node)
                else:
                    root.right = add_node

        walk(self.root, node)

    def contains(self, value):
        if self.root is None:
            return False

        def walk(root, value):
            if root.value == value:
                return True
            elif value < root.value:
                if root.left:
                    return walk(root.left, value)
            elif value > root.value:
                if root.right:
                    return walk(root.right,value)
            return False

        return walk(self.root, value)
        
class Queue:
  def __init__(self, front=None, rear=None):
    self.front = front
    self.rear = rear
    
  def enqueue(self, value):
    node = Node(value)
    if self.rear is None:
      self.front = node
      self.rear = node
    else:
      self.rear.next = node
      self.rear = self.rear.next

  def dequeue(self):
    if self.front is None:
      raise Exception('Queue is empty')
    else:
        temp = self.front
        self.front = temp.next
        temp.next = None
    return temp.value

    
  def isEmpty(self):
    return self.front == None


def breadth_first(tree):
  queue = Queue()
  tree_values = []
  
  if tree.root is None:
    raise Exception('Tree is empty')
  queue.enqueue(tree.root)
  count = 0
  
  while not queue.isEmpty():
    count+=1
    print(f'count: {count}')
    print(f'Q front: {queue.front.value}')
    print(f'Q rear: {queue.rear}')
    
    front_node = queue.dequeue()
    tree_values.append(front_node.value)
    
    if front_node.left is not None:
      print('I am in the left if')
      queue.enqueue(front_node.left)
      print(queue.isEmpty())

    if front_node.right is not None:
      print('I am in the right if')
      queue.enqueue(front_node.right)
      print(queue.isEmpty())
  return tree_values

class KaryTree:
    def __init__(self, root=None):
        self.root = root


def fizz_buzz_tree(tree):
    if tree.root is None:
        return KaryTree()
    else:
        result = KaryTree(tree.root)
        q = Queue()
        q.enqueue(tree.root)
        while not q.is_empty():
            front = q.dequeue()
            for child in front.children:
                q.enqueue(child)
            print(type(front.value))
            if front.value % 15 == 0:
                front.value = "FizzBuzz"
            elif front.value % 5 == 0:
                front.value = "Buzz"
            elif front.value % 3 == 0:
                front.value = "Fizz"
            else:
                front.value = str(front.value)
        return result  


if __name__ == '__main__':
    pass

                          