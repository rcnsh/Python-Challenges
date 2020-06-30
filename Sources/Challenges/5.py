#Write a program that will ask for anumber of days and then will show how many009hours, minutes and seconds are in that number of days.

days = int(input("How many days?"))
hours = days*24
minutes = hours*60
seconds = minutes*60
print("There are",hours,"hours,",minutes,"minutes and",seconds,"seconds in the amount of days provided.")
