# linked list zip
Create a function that takes two linked lists and returns a new linked list zipped.
## Whiteboard Process
![pic](/Challenge/linked_list/Zip.jpg)
## Approach & Efficiency
Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the zipped list.
<br> 
The Big O:<br>
time:O(n)<br>
Space:O(1)

## Solution
***Code***
```
 def zip_lists(self,list_one, list_two):
      current_one = list_one.head
      current_two = list_two.head
      result = LinkedList()
      while current_one or current_two:
          if current_one:
             result.insert(current_one.value)
             current_one = current_one.next
          if current_two:
             result.insert(current_two.value)
             current_two = current_two.next
      return result
```
***Test*** 
```
def test_zip_same():
    newList = LinkedList()
    ll1 = LinkedList()
    ll1.insert(1)
    ll1.insert(3)
    ll1.insert(2)
    ll2 = LinkedList()
    ll2.insert(5)
    ll2.insert(9)
    ll2.insert(4)
    expected = newList.zip_lists(ll2, ll1)
    actual = '1 ->5 ->3 ->9 ->2 ->4 ->NULL'
    expected ==  actual


def test_zip_ll2_shorter():
    newList = LinkedList()
    ll1 = LinkedList()
    ll1.insert(7)
    ll1.insert(8)
    ll1.insert(6)
    ll2 = LinkedList()
    ll2.insert(0)
    ll2.insert(11)
    expected = newList.zip_lists(ll2, ll1)
    actual = '7 ->0 ->8 ->11 ->6 ->NULL'
    expected ==  actual


def test_zip_ll1_shorter():
    newList = LinkedList()
    ll1 = LinkedList()
    ll1.insert(12)
    ll1.insert(13)
    ll1.insert(22)
    ll2 = LinkedList()
    ll2.insert(25)
    ll2.insert(29)
    ll1.insert(32)
    ll1.insert(62)
    expected = newList.zip_lists(ll2, ll1)
    actual = '12 ->25 ->13 ->29 ->22 ->32 ->62 ->NULL'
    expected ==  actual
```
