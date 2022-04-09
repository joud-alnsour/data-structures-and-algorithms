# Stacks and Queues and PseudoQueue and Animal Shelter
**Stack:**<br>
A stack is a limited access data structure - elements can be added and removed from the stack only at the top. push adds an item to the top of the stack, pop removes the item from the top. <br>

**Queue:**<br>
 New additions to a line made to the back of the queue, while removal (or serving) happens in the front. In the queue only two operations are allowed enqueue and dequeue. Enqueue means to insert an item into the back of the queue, dequeue means removing the front item.<br>

 **Validate Brackets:**<br>
function called validate brackets

**Animal Shelter**<br>
Create a class called AnimalShelter which holds only dogs and cats.
The shelter operates using a first-in, first-out approach.
## Challenge
- Create a Node class , class Stack , class Queue , class PseudoQueue
- have (push,pop,peek,is empty) methods inside class Stack 
- have (enqueue,dequeue,peek,is empty) methods inside class Queue
- have (enqueue,dequeue,peek,is empty) methods inside class PseudoQueue
**validate brackets**
- function called validate brackets:
   - Arguments: string
   - Return: boolean
- The method will return a true if (), {}, and [] are balanced. Also need to check the order of the braces, so ({)} would still False.<br>
**Animal Shelter**<br>
- have (enqueue,dequeue) methods inside class AnimalShelter

## Approach & Efficiency
Big O <br>
time:O(1)<br>
space:O(1)<br>
**validate brackets**<br>
The method will loop through the string, stacking the opening braces. When the loop reaches a closing brace, it will pop the stack and compare it to the previous one.
Big O<br>
time:O(n)<br>
space:O(n)<br>
**Animal Shelter**<br>
Big O for enqueue<br> 
time:O(1)<br>
space:O(1)<br>
Big O for dequeue<br>
time:O(n)<br>
space:O(n)<br>
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
        if not isinstance(animal,Cat) and not isinstance(animal,Dog):
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

``` 
***Test Animal Shelter***
``` 
def test_animal():
    animal = AnimalShelter()
    [animal.enqueue(j) for j in [Cat(),Dog(),Dog()]]
    assert str(animal.sanctuary.peek()) == 'cat'

def test_animal_dequeue():
    animal = AnimalShelter()
    [animal.enqueue(j) for j in [Cat(),Dog(),Dog()]]
    assert str(animal.dequeue('dog')) == 'dog'
    assert str(animal.sanctuary.peek()) == 'cat'

def test_animle_dequeue():
    animal = AnimalShelter()
    [animal.enqueue(j) for j in [Cat(),Dog(),Dog()]]
    assert str(animal.dequeue('cat')) == 'cat'
    assert str(animal.dequeue('fish')) == 'dog'

def test_animal_empty():
    with pytest.raises(Exception):
        animal = AnimalShelter()
        assert animal.dequeue()
   
```
> Solution for Code Challenge: Class 13<br>

***Code validate brackets***
``` 
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
   
def test_empty_string():
    string = ""
    actual = validate_brackets(string)
    expected = True
    assert actual == expected 

``` 