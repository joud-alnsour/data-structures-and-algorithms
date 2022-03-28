class Node:
 


    def __init__(self,value):
        self.value = value
        self.next = None


class Stack():
    """
    Stack property: top
    Stack methods:
    - push
        - Arguments: value
        - adds a new node with that value to the top of the stack with an O(1) Time performance.
    - pop
        - Arguments: none
        - Returns: the value from node from the top of the stack
        - Removes the node from the top of the stack
        - Should raise exception when called on empty stack
    - peek
        - Arguments: none
        - Returns: Value of the node located at the top of the stack
        - Should raise exception when called on empty stack
    - is_empty
        - Arguments: none
        - Returns: Boolean indicating whether or not the stack is empty.
    """

    def __init__(self, top=None):
        self.top = top


    def push(self, value):
        node = Node(value)
        if self.is_empty():
            self.top = node
        else:
            node.next = self.top
            self.top = node


    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop an empty stack")
        else:
            popped = self.top
            self.top = popped.next
            popped.next = None
            return popped.value


    def peek(self):
        if self.is_empty():
            raise Exception("Cannot peek an empty stack")
        else:
            return self.top.value
        

    def is_empty(self):
        return self.top == None

    
class Queue:
    """
    Queue property: front, rear
    Queue methods:
    - enqueue
        - arguments: value
        - adds a new node with that value to the back of the queue with an O(1) Time performance
    - dequeue
        - Arguments: none
        - Returns: the value from node from the front of the queue
        - Removes the node from the front of the queue
        - Should raise exception when called on empty queue
    - peek
        - Arguments: none
        - Returns: Value of the node located at the front of the queue
        - Should raise exception when called on empty stack
    - is_empty
        - Arguments: none
        - Returns: Boolean indicating whether or not the queue is empty
    """
    
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Cannot dequeue an empty queue")
        else:
            dequeued = self.front
            self.front = dequeued.next
            dequeued.next = None
            return dequeued.value

    def peek(self):
        if self.is_empty():
            raise Exception("Cannot peek an empty queue")
        else:
            return self.front.value

    def is_empty(self):
        return self.front == None


class PseudoQueue:
    """
    Implement Queue with two Stacks
    Queue methods:
    - enqueue
        - arguments: value
    - dequeue
        - Arguments: none
        - Returns: the value from node from the front of the queue
        - Removes the node from the front of the queue
        - Should raise exception when called on empty queue
    - peek
        - Arguments: none
        - Returns: Value of the node located at the front of the queue
        - Should raise exception when called on empty stack
    - is_empty
        - Arguments: none
        - Returns: Boolean indicating whether or not the queue is empty
    """

    def __init__(self):
        self.storage = Stack()
        self.reversed_storage = Stack()
        self.front_value = None

    def enqueue(self, value):
        if self.storage.top == None:
            self.front_value = value 
        self.storage.push(value)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Cannot dequeue an empty queue")
        else:
            while self.storage.top != None:
                self.reversed_storage.push(self.storage.pop())
            dequeued_value = self.reversed_storage.pop()
            if self.reversed_storage.top:
                self.front_value = self.reversed_storage.peek()
            else:
                self.front_value = None
            while self.reversed_storage.top != None:
                self.storage.push(self.reversed_storage.pop())
            return dequeued_value

    def peek(self):
        if self.is_empty():
            raise Exception("Cannot peek an empty queue")
        else:
            return self.front_value

    def is_empty(self):
        return self.storage.top == None
                

if __name__ == '__main__':
   pass                     