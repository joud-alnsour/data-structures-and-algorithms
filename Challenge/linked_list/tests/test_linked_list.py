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


def test_append():
    ll = LinkedList()
    ll.append(Node('list')) 
    ll.append(Node('python'))
    ll.append(Node('fix'))
    actual =ll.to_string()
    expected = 'list ->python ->fix ->NULL'
    assert actual == expected




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
    actual = newList.zip_lists(ll2, ll1)
    expected = '5 ->1 ->9 ->3 ->4 ->2 ->NULL'
    assert actual ==  expected


def test_zip_ll2_shorter():
    newList = LinkedList()
    ll1 = LinkedList()
    ll1.insert(7)
    ll1.insert(8)
    ll1.insert(6)
    ll2 = LinkedList()
    ll2.insert(0)
    ll2.insert(11)
    actual = newList.zip_lists(ll2, ll1)
    expected = '7 ->0 ->8 ->11 ->6 ->NULL'
    assert actual ==  expected


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
    actual = newList.zip_lists(ll2, ll1)
    expected = '12 ->25 ->13 ->29 ->22 ->32 ->62 ->NULL'
    assert actual ==  expected
