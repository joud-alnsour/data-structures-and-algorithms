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


def test_zip_lists_new_with_both_empty_lists(empty_ll):
    result = zip_lists(empty_ll, empty_ll)
    assert result.head == None

def test_zip_lists_new_with_empty_first_ll(empty_ll, ll_with_1_3_5):
    result = zip_lists(empty_ll, ll_with_1_3_5)
    print(result.head.value)
    assert ll_with_1_3_5.head.value == 1
    assert result.head.value == 1
    assert result.head.next.value == 3
    assert result.head.next.next.value == 5
    assert result.head.next.next.next == None

def test_zip_lists_new_with_empty_second_ll(ll_with_1_3_5, empty_ll):
    result = zip_lists(ll_with_1_3_5, empty_ll)
    assert result.head.value == 1
    assert result.head.next.value == 3
    assert result.head.next.next.value == 5
    assert result.head.next.next.next == None

def test_zip_lists_same_length(ll_with_1_3_5, ll_with_2_4_6):
    result = zip_lists(ll_with_1_3_5, ll_with_2_4_6)
    assert result.head.value == 1
    assert result.head.next.value == 2
    assert result.head.next.next.value == 3
    assert result.head.next.next.next.value == 4
    assert result.head.next.next.next.next.value == 5
    assert result.head.next.next.next.next.next.value == 6
    assert result.head.next.next.next.next.next.next == None

def test_zip_lists_new_longer_first_ll(ll_with_1_3_5, ll_with_2):
    result = zip_lists(ll_with_1_3_5, ll_with_2)
    assert result.head.value == 1
    assert result.head.next.value == 2
    assert result.head.next.next.value == 3
    assert result.head.next.next.next.value == 5
    assert result.head.next.next.next.next == None

def test_zip_lists_new_longer_second_ll(ll_with_1, ll_with_2_4_6):
    result = zip_lists_new(ll_with_1, ll_with_2_4_6)
    assert result.head.value == 1
    assert result.head.next.value == 2
    assert result.head.next.next.value == 4
    assert result.head.next.next.next.value == 6
    assert result.head.next.next.next.next == None

@pytest.fixture
def empty_ll():
    ll = LinkedList()
    return ll

@pytest.fixture
def ll_with_1_3_5():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(5)
    return ll

@pytest.fixture
def ll_with_2_4():
    ll = LinkedList()
    ll.append(2)
    ll.append(4)
    return ll

@pytest.fixture
def ll_with_2_4_6():
    ll = LinkedList()
    ll.append(2)
    ll.append(4)
    ll.append(6)
    return ll

@pytest.fixture
def ll_with_1():
    ll = LinkedList()
    ll.append(1)
    return ll

@pytest.fixture
def ll_with_2():
    ll = LinkedList()
    ll.append(2)
    return ll

