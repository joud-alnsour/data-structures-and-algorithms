# Insert to Middle of an Array
Create a BinarySearch function that takes two parameters: a sorted array and the search key. Return the index of the array's element that is equal to the value of the search key, or -1 if the element is not in the array, without using any of your language's built-in functions.

## Whiteboard Process
![pic](/Challenge/binary.jpg)
## Approach & Efficiency
 We want to use binary search to find the element we need. As a result, we must divide the array into two parts and determine if the element is the middle element, in which case the index we return is the middle element's index, or if it is less than the middle, in which case we must continue searching on the right half or the left half.
<br> 
The Big O: time:O(1).<br>
Space: O(1)
