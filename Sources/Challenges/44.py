question = "y"
howmany = 0
while question == "y":
    someone = input("Invite someone to the party!")
    print (someone, "has been invited! :)")
    howmany = howmany + 1
    question = input("Do you want to invite someone else?")
print("So far, you have, ",howmany, "people coming to your party!")