def hoarePartition(arr, low, high):
    p = arr[low]
    i, j = low-1, high+1

    while True:
        i = i+1
        while arr[i]<p: i = i+1
        j = j-1
        while arr[j]>p: j = j-1

        if i>=j: return j
        arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr, low, high):
    if low<high:
        pivot = hoarePartition(arr, low, high)

        quickSort(arr, low, pivot)
        quickSort(arr, pivot+1, high)

def sort(arr):
    quickSort(arr, 0, len(arr)-1)


if __name__=='__main__':
    arr = [10,5,98,32,22,87,5,6,9]
    sort(arr)
    print(arr)