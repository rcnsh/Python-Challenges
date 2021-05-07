import random

num1=random.randint(1,100)
num2=random.randint(1,100)
num3=random.randint(1,100)
num4=random.randint(1,100)
num5 = num1

print("Enter one of these numbers:")

mylist = [[num1], [num2], [num3], [num4]]
random.shuffle(mylist)

for x in mylist:
    print(x[0])

