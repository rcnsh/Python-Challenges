import random

matchsticks = 27
playersturn = 1

while matchsticks > 0:

    if playersturn == 1:
        askp1 = int(input("P1 Pick a number of sticks to pick up: "))
        if askp1 < 4 and askp1 > 0:
            matchsticks = matchsticks - askp1
            playersturn = playersturn + 1
            print("There are now", matchsticks, "remaining!")
        else:
            print("You have to pick a number between 1 and 3")

    elif playersturn == 2:
        askp2 = random.randint(1,3)
        print("AI picked", askp2)
        matchsticks = matchsticks - askp2
        playersturn = playersturn - 1
        print("There are now", matchsticks, "remaining!")
    
print(playersturn, "wins! gg")