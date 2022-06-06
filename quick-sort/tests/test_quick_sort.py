import pytest
from quick_sort.quick_sort import QuickSort


def test_quick_sort_fails():
    with pytest.raises(Exception):
        QuickSort(20)

 
def test_sample_array(sample_array):
    assert QuickSort(sample_array, 0, 5) == [4, 8, 15, 16, 23, 42]



@pytest.fixture
def sample_array():
    return [8,4,23,42,16,15]


def test_Quick():
    assert QuickSort([8,4,23,42,16,15],0,5) == [4, 8, 15, 16, 23, 42]
    #Reverse-sorted
    assert QuickSort([20,18,12,8,5,-2],0,5) == [-2, 5, 8, 12, 18, 20]
    #Few uniques
    assert QuickSort([5,12,7,5,5,7],0,5) == [5, 5, 5, 7, 7, 12]
    #Nearly-sorted
    assert QuickSort([2,3,5,7,13,11],0,5) == [2, 3, 5, 7, 11, 13]    


   