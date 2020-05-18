import random

number = random.randint(1,10)
guess = 0
count = 0


while guess != number and guess != "exit":
    guess = input("What's your guess? (1-10)")
    
    if guess == "exit":
        break
    
    guess = int(guess)
    count += 1
    
    if guess < number:
        print("wrong")
    elif guess > number:
        print("wrong!")
    else:
        print("correct!")