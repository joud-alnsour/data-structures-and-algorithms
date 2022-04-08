# Stacks and Queues and PseudoQueue
**Stack:**<br>
A stack is a limited access data structure - elements can be added and removed from the stack only at the top. push adds an item to the top of the stack, pop removes the item from the top. <br>

**Queue:**<br>
 New additions to a line made to the back of the queue, while removal (or serving) happens in the front. In the queue only two operations are allowed enqueue and dequeue. Enqueue means to insert an item into the back of the queue, dequeue means removing the front item.<br>

 **Validate Brackets:**<br>
function called validate brackets

## Challenge
- Create a Node class , class Stack , class Queue , class PseudoQueue
- have (push,pop,peek,is empty) methods inside class Stack 
- have (enqueue,dequeue,peek,is empty) methods inside class Queue
- have (enqueue,dequeue,peek,is empty) methods inside class PseudoQueue
**validate brackets**
- function called validate brackets:
   - Arguments: string
   - Return: boolean
- The method will return a true if (), {}, and [] are balanced. Also need to check the order of the braces, so ({)} would still False.
## Approach & Efficiency
Big O <br>
time:O(1)<br>
space:O(1)<br>
**validate brackets**
The method will loop through the string, stacking the opening braces. When the loop reaches a closing brace, it will pop the stack and compare it to the previous one.
Big O<br>
time:O(n)<br>
space:O(n)
## API
**Stack methods API**
- Stack instance variable: top
- push
    - Arguments: value
    - adds a new node with that value to the top of the stack with an O(1) Time performance
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
   - Returns: Boolean indicating whether or not the stack is empty


**Queue methods API**
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

**PseudoQueue methods API**
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

## Whiteboard Process

**PseudoQueue**

![pic](/stack_and_queue/PseudoQueue.jpg)

**AnimalShelter**<br>

![pic](/stack_and_queue/AnimalShelter.jpg)

**validate brackets**<br>

![pic](/stack_and_queue/ValidateBrackets.jpg)

## Solution
***Code PseudoQueue***
```
class PseudoQueue:
 

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
```
***Test PseudoQueue***  
``` 
def test_pseudo_queue():
    pseudo = PseudoQueue()
    assert pseudo


def test_pseudo_queue_enqueue():
    pseudo = PseudoQueue()
    pseudo.enqueue('a')
    assert pseudo.dequeue() == 'a'


def test_pseudo_queue_enqueue_multi():
    pseudo = PseudoQueue()
    pseudo.enqueue('a')
    pseudo.enqueue('b')
    pseudo.enqueue('c')
    assert pseudo.dequeue() == 'a'
    assert pseudo.dequeue() == 'b'
    assert pseudo.dequeue() == 'c'


def test_pseudo_queue_dequeue():
    pseudo = PseudoQueue()
    pseudo.enqueue(1)
    assert pseudo.dequeue() == 1


def test_pseudo_queue_dequeue_multi():
    pseudo = PseudoQueue()
    pseudo.enqueue(3)
    pseudo.enqueue(2)
    pseudo.enqueue(1)
    assert pseudo.dequeue() == 3
    assert pseudo.dequeue() == 2
    assert pseudo.dequeue() == 1
```    
***Code Animal Shelter***
```
class Dog():
    def __init__(self):
        self.animal_name = "dog"

class Cat():
    def __init__(self):
        self.animal_name = "cat"
  
class AnimalShelter():
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, animal):
        if animal != 'dog' and animal != 'cat':
            return None
        while self.in_stack.top:
            newValue = self.in_stack.pop()
            self.out_stack.push(newValue)
        self.in_stack.push(animal)
        while self.out_stack.top:
            newValue = self.out_stack.pop()
            self.in_stack.push(newValue)

    def dequeue(self, pref):
        if pref != 'dog' and pref != 'cat':
            return None
        elif pref == 'cat' and self.in_stack.top == 'cat':
            self.in_stack.pop()
        elif pref == 'dog' and self.in_stack.top == 'dog':
            self.in_stack.pop()

``` 
***Test Animal Shelter***
``` 
def test_animal_shelter():
    animal_shelter = AnimalShelter()
    assert animal_shelter
def test_animal_shelter_enqueue_cat():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('cat')
    actual = animal_shelter.in_stack.peek()
    expected = 'cat'
    assert actual == expected
def test_animal_shelter_enqueue_dog():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('dog')
    actual = animal_shelter.in_stack.peek()
    expected = 'dog'
    assert actual == expected
def test_animal_shelter_enqueue_multiple():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('dog')
    animal_shelter.enqueue('cat')
    actual = animal_shelter.in_stack.peek()
    expected = 'dog'
    assert actual == expected
def test_animal_shelter_enqueue_return_none():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('dog')
    actual = animal_shelter.in_stack.peek()
    expected = 'cat'
    assert actual != expected

def test_animal_shelter_dequeue():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('dog')
    animal_shelter.enqueue('cat')
    animal_shelter.enqueue('cat')
    actual = animal_shelter.dequeue('cat')
    expected = 'cat'
    assert actual == expected
   
```
> Solution for Code Challenge: Class 13<br>

***Code validate brackets***
``` 
def validate_brackets(string):
    open_tags = ["{","[","("]
    closing_tags = ["}","]",")"]
    validate = []

    for i in string:
        if i in open_tags:
            validate.append(open_tags.index(i))
            print(f"Validate open tags in this way: {open_tags.index(i)}")


        elif i in closing_tags:
            if ((len(validate) > 0) and (closing_tags.index(i) == validate[-1])):
                print(f"Validate the closing tags in this way: {closing_tags.index(i)}")
                validate.pop()
            else:
                return False

    if len(validate) == 0:
        return True
    else:
        return False

``` 
***Test validate brackets***
```
def test_string_one():
    string = "{[]{()}}"
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_string_two():
    string = "[[()]]"
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_string_three_spaces():
    string = "{ [ ) )"
    actual = validate_brackets(string)
    expected = False
    assert actual == expected

def test_empty_string():
    string = ""
    actual = validate_brackets(string)
    expected = True
    assert actual == expected 
``` 