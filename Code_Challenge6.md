# linked list insertions
- Append:<br>
Create an append method for the Linked List class that takes one argument (value) and adds a new node at the end of the list with the given value.
- Insert Before:<br>
Createa method (insert_befor) for the Linked List class that takes two arguments (new, value) then insert the (new) before the (value) of the linked list if it does exist
- Insert After:<br>
Create a method for the Linked List class called insert_after that takes two arguments (old , new) and inserts the (old) after the (new) of the linked list if it exists.
# Whiteboard Process
- Append:

![pic](/Challenge/linked_list/append.jpg)
<br>

- Insert Before:

![pic](/Challenge/linked_list/befor.jpg)
<br>

- Insert After:

![pic](/Challenge/linked_list/after.jpg)

## Approach & Efficiency
- Append:<br>
We begin by determining whether the input is None. If that's the case, we'll make an exception. then see if the input is a member of the class (Node). If it isn't, we will make it one. The linked list is then checked to see if it is empty. If that's the case, move the new value to the top of the linked list.
- Insert Before:<br>
Determine whether one of the inputs is None. If that's the case, make an exception. Verify that each of the inputs is a class instance (Node). If it isn't already one, make it one. Verify that the (value) is present in the linked list. Raise an exception if it doesn't. Verify that the linked list isn't empty. If that's the case, move the new value to the top of the linked list.
- Insert After:<br>
Look to see if one of the inputs is None. If that's the case, make an exception. Verify that each of the inputs is a class instance (Node). If it isn't already one, make it one. Verify that the (value) is present in the linked list. Raise an exception if it doesn't. Verify that the linked list isn't empty. If that's the case, move the new value to the top of the linked list.

<br> 

- The Big O for (Append,Insert Before,Insert After):<br> 
     - time:O(n)<br>
     - Space: O(n)

## Solution
- Append:<br>

***Code Append***
```
    def append(self,value):
        if value == '':
            raise TypeError('Node not empty')
        else:
            
            if self.head is None:
                self.head = value
            
            else:
                current = self.head
                while current.next :
                    current = current.next
                current.next = value   

```
***Test Append***  
``` 
def test_append():
    ll = LinkedList()
    ll.append(Node('list')) 
    ll.append(Node('python'))
    ll.append(Node('fix'))
    actual =ll.to_string()
    expected = 'list ->python ->fix ->NULL'
    assert actual == expected
```    
- Insert Before:<br>

***Code Insert Before***
```
 def insert_befor(self, value , new):
        value = Node(value)
        new = Node(new)
        if self.head == None:
            return

        if self.head.value == value:
            return

        current =  self.head
        if current.value== value:
            new.next= current
            self.head=new
        while current:
            if current.next.value == value.value: 
                new.next= current.next
                current.next = new    
                return 
            current = current.next   
```
***Test Insert Before*** 
```
def test_insert_befor():
    ll = LinkedList()
    ll.insert('python')
    ll.insert('add')
    ll.insert('joud')
    ll.insert_befor('python' , 'language')
    actual = ll.__str__()
    expected ='joud ->add ->language ->python ->NULL'
    assert actual == expected  
```
- Insert After:<br>

***Code Insert After***
```
  def insert_after(self, old , new):
      
        if new == None:
            raise TypeError('value is empty')
        if old == None:
            raise TypeError('value is empty')
        else:
            old = Node(old)
            new = Node(new)
            current =  self.head
        while current:
            if current.value == old.value:
                new.next = current.next
                current.next = new
            current = current.next
        return
```
***Test Insert After*** 
```
def test_insert_after():
    ll = LinkedList()
    ll.insert('python')
    ll.insert('add')
    ll.insert('joud')
    ll.insert_after('add' , 'nice')
    actual = ll.__str__()
    expected = 'joud ->add ->nice ->python ->NULL'
    assert actual == expected
```

