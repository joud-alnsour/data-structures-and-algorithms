# linked list kth
Create a function (get_kth_from_end) that takes a single argument (k), a positive integer, and returns the (k)th member from the list's tail.

## Whiteboard Process
![pic](/Challenge/linked_list/kth.jpg)
## Approach & Efficiency
Create a function (get_kth_from_end) within the class (LinkedList) that takes one argument (k), the index from the left, and checks if the input is a positive integer.
<br> 
The Big O: time:O(n).<br>
Space: O(n)

## Solution
***Code***
```
def test_kth_out_of_range():
    with pytest.raises(Exception):
        ll=LinkedList() 
        ll.insert('language')        
        ll.insert('best')
        ll.insert('a')
        ll.insert('python')
        actual = ll.get_kth_from_end(5)
        expected = 'The index is out of bounds'
        assert actual ==  expected

def test_kth_same_to_lengh():
    with pytest.raises(Exception):
        ll=LinkedList() 
        ll.insert('language')        
        ll.insert('best')
        ll.insert('a')
        ll.insert('python')
        actual = ll.get_kth_from_end(3)
        expected = 'language'
        assert actual ==  expected


def test_kth_not_positive():
    with pytest.raises(Exception):
        ll=LinkedList() 
        ll.insert('language')        
        ll.insert('best')
        ll.insert('a')
        ll.insert('python')
        actual = ll.get_kth_from_end(-2)
        expected = 'the index must be positive'
        assert actual ==  expected

def test_kth_one_node():
    ll=LinkedList() 
    ll.insert('language')        
    actual = ll.get_kth_from_end(0)
    expected = 'language'
    assert actual ==  expected

def test_kth_middle():
    ll=LinkedList() 
    ll.insert('language')        
    ll.insert('best')
    ll.insert('good')
    ll.insert('is')
    ll.insert('python')
    actual = ll.get_kth_from_end(2) 
    expected =  'good'
    assert actual ==  expected
```    

