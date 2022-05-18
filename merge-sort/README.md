# Challenge Summary
 Create a Merge Sort algorithm that accepts an array as input and outputs a sorted array.
## Whiteboard Process
 ![pic](/merge-sort/assets/MergeSort.jpg)
## Approach & Efficiency
 Big O<br>
time:O(n)<br>
space:O(n)<br>
## Solution
***Code***
```
def Mergesort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        Mergesort(left)
        Mergesort(right)
        merge(left, right, arr)
    return arr
        
def merge(left,right,arr):
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
```
***Test***  
```
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

```


- [x] done README file 
- [x] done BLOG  
- [x] done Whiteboard
- [x] done the test 
- [x] done the code 