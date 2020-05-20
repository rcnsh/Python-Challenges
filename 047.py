#Ask the user to enter a number and then enter 
# another number. Add these two numbers together and 
# then ask if they want to add another number. 
# If they enter “y", ask them to enter another number 
# and keep adding numbers until they do not answer “y”. 
# At the end display the total.

num1 = int(input("Pick a number"))
num2 = int(input("Pick another number"))

again = "y"
while again == "y":
    num  = int(input("Do you want to add another number?"))
