array = [1, 5, 6, 8, 10, 22, 67, 80, 82, 100, 102, 110, 150,151,152,153,154,155,156,157,158,159,160]

def searcharray(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while (start <= end):
        print("Subarray in step {}: {}".format(step, str(array[start:end+1])))
        step += 1
        mid = (start + end) // 2

        if element == array[mid]:
            print("Found " + str(element))
            return mid

        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1


    print("Could not find number")
    return -1

input = int(input("Enter a number: "))
init = searcharray(array, input)

