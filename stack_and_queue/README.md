# Stacks and Queues
**Stack:**<br>
A stack is a limited access data structure - elements can be added and removed from the stack only at the top. push adds an item to the top of the stack, pop removes the item from the top. <br>
**Queue:**<br>
 New additions to a line made to the back of the queue, while removal (or serving) happens in the front. In the queue only two operations are allowed enqueue and dequeue. Enqueue means to insert an item into the back of the queue, dequeue means removing the front item.

## Challenge
- Create a Node class , class Stack , class Queue
- have (push,pop,peek,is empty) methods inside class Stack 
- have (enqueue,dequeue,peek,is empty) methods inside class Queue 
## Approach & Efficiency
Big O <br>
time:O(1)<br>
space:O(1)
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

