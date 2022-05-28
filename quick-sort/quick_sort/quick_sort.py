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

if __name__ == '__main__':
    pass