import pytest
from hashmap_left_join.hashmap_left_join import Hashtable, left_join_hash
 

def test_hashmap_left_join():
    hashmap1 = Hashtable()
    hashmap1.set('diligent', 'employed')
    hashmap1.set('fond', 'enamored')
    hashmap1.set('guide', 'usher')
    hashmap1.set('outfit', 'garb')
    hashmap1.set('wrath', 'anger')
    hashmap2 = Hashtable()
    hashmap2.set('diligent', 'idle') 
    hashmap2.set('fond', 'averse')
    hashmap2.set('guide', 'follow')
    hashmap2.set('flow', 'jam')
    hashmap2.set('wrath', 'delight')
    hashmap = left_join_hash(hashmap2, hashmap1)
    assert hashmap.get('wrath') == ['delight', 'anger']
    assert hashmap.get('fond') == ['averse', 'enamored']
    assert hashmap.get('diligent') == ['idle', 'employed']
    assert hashmap.get('guide') == ['follow', 'usher']
    assert hashmap.get('outfit') == None


def test_hashmap_left_join_collsion():
    hashmap1 = Hashtable()
    hashmap1.set('diligent', 'employed')
    hashmap1.set('fond', 'enamored')
    hashmap1.set('guide', 'usher')
    hashmap1.set('outfit', 'garb')
    hashmap1.set('wrath', 'anger')
    hashmap2 = Hashtable()
    hashmap2.set('diligent', 'idle') 
    hashmap2.set('fond', 'averse')
    hashmap2.set('guide', 'follow')
    hashmap2.set('flow', 'jam')
    hashmap2.set('wrath', 'delight')
    hashmap = left_join_hash(hashmap1, hashmap2)
    assert hashmap.get('diligent') == ['employed', 'idle']
    assert hashmap.get('diilgnte') == None

def test_left_join_empty():
    hashmap1 = Hashtable()
    hashmap2 = Hashtable()
    hashmap=left_join_hash(hashmap1, hashmap2)

    assert hashmap.keys() == []


def test_hashmap_left_join_error_1():
    with pytest.raises(Exception):
        hashmap1 = Hashtable()
        hashmap1.set('guide', 'usher')
        hashmap2 = []
        hashmap2.append(1)
        left_join_hash(hashmap1, hashmap2)

def test_hashmap_left_join_error_2():
    with pytest.raises(Exception):
        hashmap1 = Hashtable()
        hashmap1.set(2, 'employed')
        hashmap2 = Hashtable()
        hashmap2.set('fond', 'idle')
        left_join_hash(hashmap1, hashmap2)    