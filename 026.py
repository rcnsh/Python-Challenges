word = input("Enter a word")
piglatin = word[1:100] + word[0:1] + "ay"
piglatin = piglatin.lower()
print(piglatin)
