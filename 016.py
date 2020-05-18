question = input("Is it raining?")
text = question.lower()
if question == ("yes"):
    question2 = input("Is it windy?")
    text = question2.lower()
    if question2 == ("yes"):
        print ("Bring a waterproof coat")
    elif question2 == ("no"):
        print ("Bring an umbrella")

elif question == ("no"):
    print ("yay")

    
