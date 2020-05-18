import random

number = random.randint(1,9)
guess = 0



while guess != number and guess != "exit":
    guess = input("What's your guess?")
    
    if guess == "exit":
        break
    
    guess = int(guess)
    
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("correct")
        