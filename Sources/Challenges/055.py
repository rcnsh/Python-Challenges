import random

num1=random.randint (1,5)

ask = int(input("Pick a number between 1 and 5"))

while ask < num1 and ask > num1 + 1:
    print ("You win")
else:
    print("You lose...")