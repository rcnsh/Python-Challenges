import random
i = 0
while i > 0:
    num = random.randint(1,6)
    ask = input("Would you like to roll the dice?")

    if ask == "yes":
        print (num)
        i = i + 1
    elif ask == "no":
        print("Goodbye....")