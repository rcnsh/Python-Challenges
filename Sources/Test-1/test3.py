import random
import time

seconds = time.time()
word = random.choice( ["bubble", "speed", "random", "boomer", "computer", "science", "hellish", "death", "suicidal", "hopeless", "destruction", "addiction", "drugs", "impossible", "keyboard", "phones", "drugs", "market", "start", "python"] )
start = time.time()
enteringword = input(f"Enter {word} 3 times")
end = time.time()

if enteringword == word + " " + word + " " + word:
    print ("Well Done! You took", (end-start), "seconds to type that word three times!")
else:
    print ("Better luck next time! :(")
    

