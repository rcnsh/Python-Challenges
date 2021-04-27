first = input("pls enter ur first name")
if len(first) < 5:
    last = input("Enter ur last name")
    fullname = first + last
    fullname=fullname.upper()
    print(fullname)
elif len(first) > 5:
    first=first.lower()
    print(first)
