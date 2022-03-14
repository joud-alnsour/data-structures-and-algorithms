
from linked_list.linked_list import LinkedList, Node 
def test_empty_linked():
    listt= LinkedList()
    actual=listt.head
    excepted= None
    actual== excepted

def test_add():
    add= LinkedList()
    add.insert(Node('joud'))
    add.insert(Node('hello'))
    add.insert(Node('hi'))
    assert 'hi ->hello ->joud ->NULL'== add.to_string()


def test_includes():
    listt= LinkedList()
    listt.insert(Node('good'))
    assert listt.includes('good')==True
    assert listt.includes(9)==False


