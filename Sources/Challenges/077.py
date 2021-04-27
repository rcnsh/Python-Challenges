name1 = input("Enter a name of somebody you want to invite to your party: ")
name2 = input("Enter another name: ")
name3 = input("Enter a third name: ")
party=[name1,name2,name3]
another = input("Do you want to invite another (y/n): ")
while another == "y":
    newname=party.append(input("Enter another name: "))
    another = input("Do you want to invite another (y/n): ")
print("You have", len(party), "people coming to your party")
print(party)
selection = input("Enter one of the names: ")
print(selection,"is in position",party.index(selection),"on the list")
stillcome=input("Do you still want them to come (y/n): ")
if stillcome == "n":
    party.remove(selection)
print(party)





















































#Written by Nichola Lacey and copyright owned by (c) Nichola Wilkin Ltd. 2017
