matchsticks = 27
playersturn = 1

while matchsticks > 0:

    if playersturn == 1:
        askp1 = int(input("Pick a number of sticks to pick up"))
        matchsticks = matchsticks - askp1
        playersturn = playersturn + 1

    if playersturn == 2:
        askp2 = int(input("Pick a number of stick to pick up"))
        matchsticks = matchsticks - askp2

