#Augmented Heap Entry that stores the value and an index we will need
class AugmentedEntry:
    def __init__(self, value, lindex):
        self.value = value
        self.lindex = lindex
    
    def __lt__(self, other):
        return self.value<other.value
    
    def __str__(self):
        return str(self.value)

def buildHeap(arr, size):
    last_internal = (size-2)//2
    for i in range(last_internal, -1, -1):
        heapify(arr, i, size)
    return

def heapify(arr, index, size):
    left, right = 2*index+1, 2*index+2
    minimum = index

    if left<size and arr[left]<arr[minimum]:
        minimum = left
    if right<size and arr[right]<arr[minimum]:
        minimum = right
    
    if minimum!=index:
        arr[index], arr[minimum] = arr[minimum], arr[index]
        heapify(arr, minimum, size)

def decreaseKey(arr, index):
    #If index is already the root, return
    if index==0: return
    parent = (index-1)//2
    if arr[index]<arr[parent]:
        arr[index], arr[parent] = arr[parent], arr[index]
        decreaseKey(arr, parent)

def heappush(arr, element):
    arr.append(element)
    decreaseKey(arr, len(arr)-1)

def heappop(arr):
    if len(arr)==0: return []
    element = arr[0]
    arr[0] = arr[-1]
    arr.pop()
    heapify(arr, 0, len(arr)-1)
    return element

if __name__=='__main__':
    arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
    arr = list(map(lambda x: AugmentedEntry(x, 0), arr))
    buildHeap(arr, len(arr))
    print([x.value for x in arr])
    heappush(arr, AugmentedEntry(0, 0))
    print([x.value for x in arr])
    print(heappop(arr))
    print([x.value for x in arr])