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
    
                
# new code
class Dog():
    def __init__(self):
        self.animal_name = "dog"

    def __str__(self):
        return f'{self.animal_name}'    

class Cat():
    def __init__(self):
        self.animal_name = "cat"

    def __str__(self):
        return f'{self.animal_name}'    
  
class AnimalShelter():
    def __init__(self):
        self.sanctuary = Queue()
        self.dog = Dog()
        self.cat = Cat()

    def __str__(self):
        return f'{self.sanctuary}'    

    def enqueue(self, animal):
        if isinstance(animal,Cat) and isinstance(animal,Dog):
            return ('just a cat or a dog')
        else:
            self.sanctuary.enqueue(animal)

    def dequeue(self, pref= 'fish'):
        if pref != 'dog' and pref != 'cat':
            if not self.sanctuary.is_empty():
                return self.sanctuary.dequeue()
            else:
                return None
        if str(self.sanctuary.peek()) == pref:
            return self.sanctuary.dequeue()

        new = self.sanctuary.front
        previous = None
        while new:
            
            if str(new.value) == pref:
                previous.next = new.next
                new.next = None   
                return new.value
            previous = new
            new = new.next
                
        if not self.sanctuary.is_empty():
                raise Exception (f'animal shelter dont have {pref}') 
        
        else:
                raise Exception ('animal shelter is empty')   

def validate_brackets(string):
    open_tags = ["{","[","("]
    closing_tags = ["}","]",")"]
    validate  = Stack()

    if type(string) != str:
        raise Exception('just strings')
  
    for icon in string:

        if icon in open_tags:
            validate .push(icon)

        elif icon in closing_tags:
            if not validate .is_empty():
                return True

            elif icon == ')':
                if validate .top.value == '(':
                    validate .pop()    

            elif icon == '}':                
                if validate .top.value == '{':
                    validate .pop()
                    
            elif icon == ']':
                if validate .top.value == '[':
                    validate .pop()
            

    if not validate .is_empty():
        return False
    else:     
        return True


if __name__ == '__main__':
   pass               