import random

q1n1=random.randint(0,100)
q1n2=random.randint(0,100)
q2n1=random.randint(0,100)
q2n2=random.randint(0,100)
q3n1=random.randint(0,100)
q3n2=random.randint(0,100)
q4n1=random.randint(0,100)
q4n2=random.randint(0,100)
q5n1=random.randint(0,100)
q5n2=random.randint(0,100)
q6n1=random.randint(0,100)
q6n2=random.randint(0,100)
q7n1=random.randint(0,100)
q7n2=random.randint(0,100)
q8n1=random.randint(0,100)
q8n2=random.randint(0,100)
q9n1=random.randint(0,100)
q9n2=random.randint(0,100)
q10n1=random.randint(0,100)
q10n2=random.randint(0,100)

ans1 = q1n1+q1n2
ans2 = q2n1+q2n2
ans3 = q3n1+q3n2
ans4 = q4n1+q4n2
ans5 = q5n1+q5n2
ans6 = q6n1+q6n2
ans7 = q7n1+q7n2
ans8 = q8n1+q8n2
ans9 = q9n1+q9n2
ans10 = q10n1+q10n2



question1 = int(input(str(q1n1)+ "+"+ str(q1n2)))
if question1 == ans1:
    print("CORRECT!!!")
else:
    print("WRONG!!!")

question2 = int(input(str(q2n1)+ "+"+ str(q2n2)))
if question2 == ans2:
    print("CORRECT!!!")
else:
    print("WRONG!!!")

question3 = int(input(str(q3n1)+ "+"+ str(q3n2)))
if question3 == ans3:
    print("CORRECT!!!")
else:
    print("WRONG!!!")

question4 = int(input(str(q4n1)+ "+"+ str(q4n2)))
if question4 == ans4:
    print("CORRECT!!!")
else:
    print("WRONG!!!")
