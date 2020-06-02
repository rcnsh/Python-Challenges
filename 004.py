#Ask the user to enter two numbers. Add them together and display the answer as004“The total is [answer]”.


number1 = input(" Please Enter the First Number: ")
number2 = input(" Please Enter the second number: ")
sum = float(number1) + float(number2)
print('The sum of {0} and {1} is {2}'.format(number1, number2, sum))
