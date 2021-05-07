from array import *

limit = 0
array1 = array('i' [0])

while limit < 5:
    nums = int(input("Enter a number between 10 and 20"))
    if nums < 20 and nums > 10:
        array1.append(nums)
        limit = limit + 1
        if limit == 5:
            print("Thanks")
    else:
        print("Outside the range")
        break

