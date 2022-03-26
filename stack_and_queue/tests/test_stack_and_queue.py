from stack_and_queue.stack_and_queue import Stack, Queue
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

           

