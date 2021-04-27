from array import *
import random

rand1 = random.randint(1, 1000000)
rand2 = random.randint(1, 1000000)
rand3 = random.randint(1, 1000000)
rand4 = random.randint(1, 1000000)
rand5 = random.randint(1, 1000000)

numbers = array('i', [rand1, rand2, rand3, rand4, rand5])

for i in numbers:
    print(i)