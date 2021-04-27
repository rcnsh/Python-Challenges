name1 = input("Enter a name of somebody you want to invite to your party: ")
name2 = input("Enter another name: ")
name3 = input("Enter a third name: ")
party=[name1,name2,name3]
another = input("Do you want to invite another (y/n): ")
while another == "y":
    newname=party.append(input("Enter another name: "))
    another = input("Do you want to invite another (y/n): ")
print("You have", len(party), "people coming to your party")





















































#Written by Nichola Lacey and copyright owned by (c) Nichola Wilkin Ltd. 2017
