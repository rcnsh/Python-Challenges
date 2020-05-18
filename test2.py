fizzydrinks = [] 

while True:
    ask = input("Do you want to add an item to the list?")
    if ask == "Y":
        item = input("Enter your fizzy drink to the List: ")
    else:
        break
    fizzydrinks.append(item)
total = len(fizzydrinks)
print (total)