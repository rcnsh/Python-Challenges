username = input("Enter your Name.")
DOTM = int(input("What day of the month were you born on?"))
month = int(input("Enter the month you were born in. (as a number)"))
year = int(input("What year were you born in? (as a year. e.g. 2005)"))
year = year + 100
print(username, "you will get your 100th birthday card on the ", DOTM, "th, of ", month, ", ", year, ".")