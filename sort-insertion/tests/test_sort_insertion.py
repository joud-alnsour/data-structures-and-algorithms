from sort_insertion.sort_insertion import insertion_sort

def test_insertion1():
    array = [1, 4, 6, -3]
    actual = insertion_sort(array)
    expected = [-3, 1, 4, 6]
    assert actual == expected

def test_insertion2():
    array = [11, 5, 17, 55, 32, 28]
    actual = insertion_sort(array)
    expected = [5, 11, 17, 28, 32, 55]
    assert actual == expected

def test_insertion3():
   
    array = [-6, 8, -3]
    actual = insertion_sort(array)
    expected = [-6, -3, 8]
    assert actual == expected
