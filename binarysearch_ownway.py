numbers = [1,5,7,8,9,10,15,31,43,67,100,110]

def searchnumber(array, goal):
    start = 0
    end = len(array)
    mid = 0
    step = 0

    while (start <= end):
        print("Searching step {}: {}".format(step, str(array[start:end+1])))
        step+=1
        mid = (start + end) // 2

        if array[mid] == goal:
            print("Found {}".format(str(goal)))
            return True
        elif array[mid] > goal:
            end = mid-1
        elif mid < goal:
            start = mid+1

    print("Could not find the goal ({})".format(str(goal)))
    return False

input = int(input("Please enter a goal number to see if it is in the array: "))
searchnumber(numbers, input)