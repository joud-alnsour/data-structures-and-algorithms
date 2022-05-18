from merge_sort.merge_sort import Mergesort

def test_merge_sort1():
    array = [7]
    actual = Mergesort(array)
    expected = [7]
    assert actual == expected    

def test_merge_sort2():
    array = [14, 8, 3, 21, 5]
    actual = Mergesort(array)
    expected = [3, 5, 8, 14, 21]
    assert actual == expected

def test_merge_sort3():
    array = [55, 68, 10, 17 ]
    actual = Mergesort(array)
    expected = [10, 17, 55, 68]
    assert actual == expected

