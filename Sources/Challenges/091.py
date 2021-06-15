import random
from array import *

num1=random.randint(1,100)
num2=random.randint(1,100)
num3=random.randint(1,100)
num4=random.randint(1,100)
num5 = num1

print("Enter one of these numbers:")

myarray = array('i',(num1,num2,num3,num4,num5))
random.shuffle(myarray)

for x in myarray:
    print(x)

asking=int(input(""))
print("")
print(myarray.count(asking))

print("^^^ - This was how many times the number appeared in the array")


