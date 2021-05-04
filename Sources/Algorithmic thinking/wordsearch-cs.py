import random


#A subroutine to replace all "-" (empty characters) with a random letter
def randomFill(wordsearch):
  LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for row in range(0,12):
    for col in range(0,12):
      if wordsearch[row][col]=="-":
        randomLetter = random.choice(LETTERS)
        wordsearch[row][col]=randomLetter


#A subroutine to output the wordsearch on screen    
def displayWordsearch(wordsearch):
  print(" _________________________")
  print("|                         |")
  for row in range(0,12):
    line="| "
    for col in range(0,12):
      line = line + wordsearch[row][col] + " "
    line = line + "|"
    print(line)
  print("|_________________________|")  
    
#A subroutine to add a word to the wordsearch at a random position
def addWord(word,wordsearch):
  row=random.randint(0,11)
  col=0
  for i in range(0,len(word)):
    wordsearch[row][col+i]=word[i]
  #CHANGE THIS CODE TO
  # ----Randomly decide where the word will start
  # ----Decide if the word will be added horizontally, vertically or diagonally
  # ----Check that the word will fit in (within the 12 by 12 grid)
  # ----Check that the word will not overlap with existing letters/words in the wordsearch
  


#Create an empty 12 by 12 wordsearch (list of lists)
wordsearch = []
for row in range(0,12):
  wordsearch.append([])
  for col in range(0,12):
    wordsearch[row].append("-")


#Adding words to our wordsearch
addWord("PYTHON",wordsearch)    
addWord("ALGORITHM",wordsearch)    
addWord("CODING",wordsearch)    
addWord("PROGRAM",wordsearch)    


#All unused spaces in the wordsearch will be replaced with a random letter
randomFill(wordsearch)


#Display the fully competed wordseach on screen
displayWordsearch(wordsearch)