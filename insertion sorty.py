arr = [12, 11, 13, 5, 6, 9, 41, 2, 3, 0, 1, 1, 1, 56, 3]

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print("Step {}: {}".format(str(j), str(arr)))
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key



insertionSort(arr)
print("Sorted array: {}".format(str(arr)))