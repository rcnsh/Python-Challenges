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
        if matchsticks == 26:
            askp2 = 1
        elif matchsticks == 25:
            askp2 = 1
        elif matchsticks == 24:
            askp2 = 3
        elif matchsticks == 23:
            askp2 = 2
        elif matchsticks == 22:
            askp2 = 1
        elif matchsticks == 21:
            askp2 = 1
        elif matchsticks == 20:
            askp2 = 3
        elif matchsticks == 19:
            askp2 = 2
        elif matchsticks == 18:
            askp2 = 1
        elif matchsticks == 17:
            askp2 = 1
        elif matchsticks == 16:
            askp2 = 3
        elif matchsticks == 15:
            askp2 = 2
        elif matchsticks == 14:
            askp2 = 1
        elif matchsticks == 13:
            askp2 = 1
        elif matchsticks == 12:
            askp2 = 3
        elif matchsticks == 11:
            askp2 = 2
        elif matchsticks == 10:
            askp2 = 1
        elif matchsticks == 9:
            askp2 = 1
        elif matchsticks == 8:
            askp2 = 3
        elif matchsticks == 7:
            askp2 = 2
        elif matchsticks == 6:
            askp2 = 1
        elif matchsticks == 5:
            askp2 = 1
        elif matchsticks == 4:
            askp2 = 3
        elif matchsticks == 3:
            askp2 = 2
        elif matchsticks == 2:
            askp2 = 1
        elif matchsticks == 1:
            askp2 = 1
        
        print("AI picked", askp2)
        matchsticks = matchsticks - askp2
        playersturn = playersturn - 1
        print("There are now", matchsticks, "remaining!")

if playersturn == 1:
    name = ("User")
else:
    name = ("AI")

print(name, "wins! gg")