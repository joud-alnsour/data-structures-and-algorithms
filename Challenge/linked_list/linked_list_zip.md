# linked list zip
Create a function that takes two linked lists and returns a new linked list zipped.
## Whiteboard Process
![pic]()
## Approach & Efficiency
Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the zipped list.
<br> 
The Big O:<br>
time:O(n)<br>
Space:O(1)

## Solution
***Code***
```
def zip_lists(list_one, list_two):
       current_one = list_one.head
       current_two = list_two.head
       new_list = LinkedList()
       while current_one or current_two:
        if current_one:
            new_list.append(current_one.value)
            current_one = current_one.next
        if current_two:
            new_list.append(current_two.value)
            current_two = current_two.next
        return new_list
```
***Test*** 
```

```
***Fixtures***
```

```