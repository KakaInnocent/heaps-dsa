# Max Heap Example
"""
Heapify is a process of creating a max-heap from a Binary Tree(or array)
Thus, the function heapify does this.
@arr: the array containing values we're inserting
@n: the new element we're inserting
@i: This is the current element selected or inserted
"""
def heapify(arr, n, i):
    #in max heap, the largest value i usually at the top.
    #We are therefore making the largest element to be equated to the current element
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
"""
insert - inserting a new element
"""
def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum):
            for i in range((size//2)-1, -1, -1):
                heapify(array, size, i)


def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
    array[i], array[size-1] = array[size-1], array[i]

    array.remove(num)

    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)

arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 2)

print("Max Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))
