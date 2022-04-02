from stack_and_queue.stack_and_queue import Stack, Queue, PseudoQueue, AnimalShelter
import pytest

def test_stack():
    stack = Stack()

def test_push_stack_multi():
  stack = Stack()
  stack.push(1)
  stack.push(2)
  stack.push(3)
  stack.push(4)
  stack.push(5)
  actual = stack.top.value
  expected = 5
  assert actual == expected 

def test_stack_empty():
    with pytest.raises(Exception):
        stack = Stack()
        stack.pop()  

def test_pop_stack():
  stack = Stack()
  stack.push(1)
  stack.push(2)
  stack.push(3)
  actual = stack.pop()
  expected = 3
  assert actual == expected 

def test_peek_stack():
  stack = Stack()
  stack.push(1)
  stack.push(2)
  stack.push(3)
  actual = stack.peek()
  expected = 3
  assert actual == expected 

def test_is_empty():
  stack=Stack()
  actual = stack.is_empty()
  expected = True
  assert actual == expected


def test_enqueue():
  queue = Queue()
  queue.enqueue("best")
  queue.enqueue("python")
  queue.enqueue("ever")
  actual = queue.rear.value
  expected = "ever"
  assert actual == expected

def test_dequeue():
  queue = Queue()
  queue.enqueue("best")
  queue.enqueue("python")
  queue.enqueue("ever")
  actual = queue.front.value
  expected = "best"
  assert actual == expected

def test_peek_queue():
  queue = Queue()
  queue.enqueue("best")
  queue.enqueue("course")
  actual = queue.front.value
  expected = "best"
  assert actual == expected

def test_is_empty_queue():
  queue = Queue()
  actual = queue.is_empty()
  expected = True
  assert actual == expected

def test_queue():
    queue = Queue()  

def test_dequeue_empty():
    with pytest.raises(Exception):
        queue = Queue()
        queue.dequeue()

#New PseudoQueue

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

# new test
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
    animal_shelter.dequeue('cat')
    actual=animal_shelter.in_stack.peek()
    expected = 'dog'
    assert actual == expected
   