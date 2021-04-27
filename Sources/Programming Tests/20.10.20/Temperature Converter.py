C= 30

def CtoF(C):
    return (C * 1.8) + 32

F = CtoF(C)

def FtoC(F):
    return (F / 1.8) - 32

print(C, "degrees C is",F, "degrees F")