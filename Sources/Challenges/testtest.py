import random
import time

i = 0
Player1Points = 0
Player2Points = 0
Player1Tiebreaker = 0
Player2Tiebreaker = 0
Winner_Points = 0


loggedin1 = False
loggedin2 = False
while loggedin1 == False:
    username = input('What is your username? ')
    password = input('What is your password? ')
    if username == 'JakeW' or username == 'LucS' or username == 'User3' or username == 'User4' or username == 'User5':
        if password == 'password':
            print('Welcome, ',username,' you have been successfully logged in.')
            loggedin1 = True
            user1 = username
        else:
            print('Incorrect password, try again')  
    else:
        print('Incorrect username, try again')

while loggedin2 == False:
    username = input('What is your username? ')
    password = input('What is your password? ')
    if username == 'JakeW' or username == 'LucS' or username == 'User3' or username == 'User4' or username == 'User5':
        if password == 'password':
            print('Welcome, ',username,' you have been successfully logged in.')
            loggedin2 = True
            user2 = username
        else:
            print('Incorrect password, try again')  
    else:
        print('Incorrect username, try again')

def roll():

    points = 0

    die1 = random.randint(1,6)

    die2 = random.randint(1,6)

    dietotal = die1 + die2

    points = points + dietotal

    if dietotal % 2 == 0:
        points = points + 10

    else:
        points = points - 5

    if die1 == die2:
        die3 = random.randint(1,6)
        points = points +die3

    return(points)


for i in range(1,10):
    Player1Points += roll()
    print('After this round ',user1, 'you now have: ',Player1Points,' Points')
    time.sleep(1)
    Player2Points += roll()
    print('After this round ',user2, 'you now have: ',Player2Points,' Points')
    time.sleep(1)

if Player1Points == Player2Points:
    while Player1Tiebreaker == Player2Tiebreaker:


        Player1Tiebreaker = random.randint(1,6)
        Player2Tiebreaker = random.randint(1,6)

    if Player1Tiebreaker > Player2Tiebreaker:
        Player2Points = 0
    elif Player2Tiebreaker > Player1Tiebreaker:
        Player1Points = 0


if Player1Points>Player2Points:
    Winner_Points = Player1Points
    winner_User = user1
    winner = (Winner_Points, user1)
elif Player2Points>Player1Points:
    Winner_Points = Player2Points
    winner = (Winner_Points, user2)
    winner_User = user2

print('Well done, ', winner_User,' you won with ',Winner_Points,' Points')
