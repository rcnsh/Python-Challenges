import statistics

while True:
    try:
        num1 = int(input("Enter a number:"))
        num2 = int(input("Enter a number:"))
        num3 = int(input("Enter a number:"))
        num4 = int(input("Enter a number:"))
        num5 = int(input("Enter a number:"))
        num6 = int(input("Enter a number:"))
        num7 = int(input("Enter a number:"))
        num8 = int(input("Enter a number:"))
        num9 = int(input("Enter a number:"))
    except ValueError:
        print("Sorry, I didnt understand that. Please start again.")
        continue
    ListOfNumbers = [num1, num2, num3, num4, num5, num6, num7, num8, num9]


    mean = statistics.mean(ListOfNumbers)
    median = statistics.median(ListOfNumbers)
    mode =statistics.mode(ListOfNumbers)

    print("The mean of this list is ", mean)
    print("The median of this list is ", median)
    print("The mode of this list is ", mode)