from array import *

nums = array('i',[4,6,8,2,5])

for i in nums:
    print(i)

num=int(input("Select one of the numbers: "))

tryagain = True
while tryagain == True:
    if num in nums:
        print("This is in position",nums.index(num))
        tryagain = False
    else:
        print("Not in array")
        num=int(input("Select one of the numbers: "))





















































#Written by Nichola Lacey and copyright owned by (c) Nichola Wilkin Ltd. 2017
