numbers = [1,2,5,18,34,2,76,0,22,23]

def findnum(number):
    for index in range(0, len(numbers)):
        if number == numbers[index]:
            return True
    return False

goal = int(input("Enter a number to check if it is in the list: "))

inarr = findnum(goal)

if inarr == True:
    print("Found " + str(goal))
else:
    print("Could not find your goal number! (" + str(goal) + ")")
