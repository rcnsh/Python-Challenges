from array import *

entering1 = int(input("Enter a number"))
entering2 = int(input("Enter a number"))
entering3 = int(input("Enter a number"))
entering4 = int(input("Enter a number"))
entering5 = int(input("Enter a number"))
getrid = int(input("Enter a number to get rid of"))

array1 = array('i',[entering1, entering2, entering3, entering4, entering5])
array1 = sorted(array1)
array1.remove(getrid)
for i in array1:
    print(i)

