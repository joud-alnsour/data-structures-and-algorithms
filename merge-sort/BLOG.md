# Merge Sort
## Pseudocode
```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```
## Process:  
``` 
Sample Array:
[8,4,23,42,16,15]   

```
## Here is an example to explain.
- **Step 1:**
  One array with the left and right symbolizing the division to start the recursion.
 ![pic](/merge-sort/assets/1.jpg)

- **Step 2:**
  In this steps we see the division happenning right away between right and left of two new arrays.
 ![pic](/merge-sort/assets/2.jpg)

- **Step 3:**
 - This is the whole process for the recursion that will be happenning. In this you can see the recursive process with arrays being divided into right and left arrays.
  ![pic](/merge-sort/assets/3.jpg)

- **Step 4:**
 - Here we start with the smallest part of the array elements. Using the key of letter like j, k, and i. This will basically compare the values on the left and right until we get the final product of our array showing it from a ascending order.
 ![pic](/merge-sort/assets/4.jpg)

- **Step 5:**
 - In the final step you can see the final result of how the array would look once this has gone through and produces an array in a ascending order.
 ![pic](/merge-sort/assets/5.jpg)
