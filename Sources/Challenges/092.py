from array import *
import random

ask1 = int(input("Enter a number:"))
ask2 = int(input("Enter a number:"))
ask3 = int(input("Enter a number:"))


nums1 = array('i'[ask1, ask2, ask3])

random1 = random.randint(1,100)
random2 = random.randint(1,100)
random3 = random.randint(1,100)
random4 = random.randint(1,100)
random5 = random.randint(1,100)

nums2 = array('i'[random1, random2, random3, random4, random5])

nums1.append(nums2)

print(nums1)