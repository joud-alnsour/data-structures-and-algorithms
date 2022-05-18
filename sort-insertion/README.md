# Challenge Summary
Create an insertion sort function that takes an array of integers as input and returns a sorted array.
## Whiteboard Process
this is whiteboard:<br>

![pic](/sort-insertion/assets/insertion_sort.jpg)
	
## Approach & Efficiency
insertion sort implementation To traverse through the array, I used two loops. To compare them and determine if the first is greater than the second, the first loop started at index 1 and the second loop started at index 0 of the same array. If it is, the two values are swapped.<br>

Big O<br>
time:O(n^2)<br>
space:O(1)<br>

## Solution
***Code***
```
def insertion_sort(array):
    for i in range(array, len(array)):
        j = i - 1
        temp = array[i]
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    return array 

```
***Test***  
``` 
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

```

- [x] done README file 
- [x] done BLOG  
- [x] done Whiteboard
- [x] done the test 
- [x] done the code 