from hash_table.hash_table import Hashtable

def test_hash_table_null():
    hash_table = Hashtable()
    actual= hash_table.get('egg')
    expected = None
    assert actual == expected
  
def test_hash_table_set():
    hash_table = Hashtable()
    hash_table.set("cat", "dog")
    actual= hash_table.get('cat')
    expected = "dog"
    assert actual == expected

def test_hash_hash():
    hash_table = Hashtable()
    hash_table.set("egg", "chicken")
    actual= hash_table.hash("cat")
    expected = 760
    assert actual == expected

def test_hash_keys():
    hash_table = Hashtable()
    hash_table.set("Elephant", "ant")
    hash_table.set("chicken", "egg")
    hash_table.set("dog", "Meat")
    hash_table.set("cat", "Mouse")
    actual= hash_table.keys()
    expected = None
    assert actual == expected

   

   


   
    

