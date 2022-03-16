import pytest
from linked_list.linked_list import LinkedList, Node 
def test_empty_linked():
    listt= LinkedList()
    actual=listt.head
    excepted= None
    actual== excepted

def test_python():
    python= LinkedList()
    python.insert(('joud'))
    python.insert(('hello'))
    python.insert(('hi'))
    assert 'hi ->hello ->joud ->NULL'== python.to_string()


def test_includes():
    listt= LinkedList()
    listt.insert(('good'))
    assert listt.includes('good')==True
    assert listt.includes(9)==False


def test_insert_after():
    ll = LinkedList()
    ll.insert('python')
    ll.insert('add')
    ll.insert('joud')
    ll.insert_after('add' , 'nice')
    actual = ll.__str__()
    expected = 'joud ->add ->nice ->python ->NULL'
    assert actual == expected

def test_insert_befor():
    ll = LinkedList()
    ll.insert('python')
    ll.insert('add')
    ll.insert('joud')
    ll.insert_befor('python' , 'language')
    actual = ll.__str__()
    expected ='joud ->add ->language ->python ->NULL'
    assert actual == expected  


# def test_append():
#     ll = LinkedList()
#     ll.append('list') 
#     ll.append('python')
#     ll.append('fix')
#     actual =ll.to_string()
#     expected = 'list ->python ->fix ->NULL'
#     assert actual == expected


def test_kth_out_of_range():
    with pytest.raises(Exception):
        ll=LinkedList() 
        ll.insert('language')        
        ll.insert('best')
        ll.insert('a')
        ll.insert('python')
        ll.get_kth_from_end(5)


def test_kth_same_to_lengh():
    with pytest.raises(Exception):
        ll=LinkedList() 
        ll.insert('language')        
        ll.insert('best')
        ll.insert('a')
        ll.insert('python')
        ll.get_kth_from_end(4)


def test_kth_not_positive():
    with pytest.raises(Exception):
        ll=LinkedList() 
        ll.insert('language')        
        ll.insert('best')
        ll.insert('a')
        ll.insert('python')
        ll.get_kth_from_end(-2)


def test_kth_one_node():
    ll=LinkedList() 
    ll.insert('language')        
    assert ll.get_kth_from_end(0) == 'language'


def test_kth_middle():
    ll=LinkedList() 
    ll.insert('language')        
    ll.insert('best')
    ll.insert('good')
    ll.insert('is')
    ll.insert('python')
    assert ll.get_kth_from_end(2) == 'good'





