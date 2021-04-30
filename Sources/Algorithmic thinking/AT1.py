matchsticks = 27
playersturn = 1

try:
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
            askp2 = int(input("P2 Pick a number of stick to pick up: "))
            if askp2 < 4 and askp2 > 0:
                matchsticks = matchsticks - askp2
                playersturn = playersturn - 1
                print("There are now", matchsticks, "remaining!")
            else:
                print("You have to pick a number between 1 and 3")
except:
    print("INPUT A NUMBER IDIOT")
    quit()

print(playersturn, "wins! gg")

