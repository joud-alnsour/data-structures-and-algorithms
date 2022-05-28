from hash_table.hash_table import Hashtable
import pytest

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

def test_hash_fail():
    with pytest.raises(Exception):
        hash_table = Hashtable()
        hash_table.set(1, "egg") 

  

def test_hash_collision():
    hash_table = Hashtable()
    hash_table.set("cat", "meow")
    hash_table.set("act", "homework")
    assert hash_table.buckets[760] == [('cat', 'meow'), ('act', 'homework')]
    assert hash_table.get("cat") == "meow"
    assert hash_table.get("act") == "homework"
