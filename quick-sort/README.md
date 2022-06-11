# Challenge Summary
Create a quicksort method that takes an array and produces a sorted array. The input is an array, and the output is a sorted array.
## Whiteboard Process
![pic](/quick-sort/assets/QuickSort.jpg)
## Approach & Efficiency
 Big O<br>
time:O(n)<br>
space:O(1)<br>
## Solution
***Code***
```
def QuickSort(arr, left, right):
    if left < right:
        position = Partition(arr, left, right)
        QuickSort(arr, left, position - 1)
        QuickSort(arr, position + 1, right)
        
    return arr


def Partition(arr, left, right):
    pivot = arr[right]
    low = left - 1
    for index in range(left, right):
        if arr[index] <= pivot:
            low += 1
            Swap(arr, index, low)

    Swap(arr, right, low + 1)
    return low + 1

def Swap(arr, index, low):
    temp =  arr[index]
    arr[index] = arr[low]
    arr[low] = temp
```
***Test***  
```
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
```