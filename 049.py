compnum = 50
guesses = 0
randomguess = int(input("What number am i thinking of?"))
while randomguess != compnum:
    if randomguess < compnum:
        print ("Too low! :(")
        guesses = guesses + 1
    elif randomguess > compnum:
        print ("Too high! :(")
        guesses = guesses + 1
guesses = guesses + 1
print ("Congratulations! You took", guesses, "attempts!")
