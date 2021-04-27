countries = ("England", "Scotland", "Ireland", "Wales", "United Kingdom")
print (countries)
ask = input("Enter the number you want to locate the country for")
ask = int(ask) - 1
print(countries[int(ask)])