ask=int(input("How many people do you want to invite to your party?"))
if ask < 10:
    for num in range (0,ask):
        person = input("Who do you want to invite?")
        print(person, "has been invited")

elif ask > 9:
    print("Too many people!!!")
