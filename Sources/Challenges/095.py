from array import *
import random
num1 = 67.46
num2 = 93.83
num3 = 27.49
num4 = 32.51
num5 = 18.49
arraychall = array('f',[num1, num2, num3, num4, num5])

asking = int(input("enter a whole number between 2 and 5"))
if asking >= 2 and asking <= 5:
    num1 = num1 / float(asking)
    num2 = num2 / float(asking)
    num3 = num3 / float(asking)
    num4 = num4 / float(asking)
    num5 = num5 / float(asking)
    print(round(num1,2))
    print(round(num2,2))
    print(round(num3,2))
    print(round(num4,2))
    print(round(num5,2))