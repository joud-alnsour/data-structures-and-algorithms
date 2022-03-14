
from linked_list.linked_list import LinkedList, Node 
def test_empty_linked():
    listt= LinkedList()
    actual=listt.head
    excepted= None
    actual== excepted

def test_python():
    python= LinkedList()
    python.insert(Node('joud'))
    python.insert(Node('hello'))
    python.insert(Node('hi'))
    assert '"hi ->hello ->joud ->NULL"'== python.to_string()


def test_includes():
    listt= LinkedList()
    listt.insert(Node('good'))
    assert listt.includes('good')==True
    assert listt.includes(9)==False


def test_insert_after():
    ll = LinkedList()
    
    ll.insert_at_beginning('python')
    ll.insert_at_beginning('add')
    ll.insert_at_beginning('joud')
    ll.insert_after('add' , 'nice')
    actual = ll.__str__()
    expected = '"{joud}-> {add}-> {nice}-> {python}-> NULL"'
    assert actual == expected

def test_insert_befor():
    ll = LinkedList()
    ll.insert_at_beginning('python')
    ll.insert_at_beginning('add')
    ll.insert_at_beginning('joud')
    ll.insert_befor('python' , 'language')
    actual = ll.__str__()
    expected ='"{joud}-> {add}-> {language}-> {python}-> NULL"'
    assert actual == expected  


def test_append1():
    ll = LinkedList()
    ll.insert_values(['list' , 'python' ])
    ll.append('fix')
    actual =ll.__str__()
    expected = '"{list}-> {python}-> {fix}-> NULL"'
    assert actual == expected      


