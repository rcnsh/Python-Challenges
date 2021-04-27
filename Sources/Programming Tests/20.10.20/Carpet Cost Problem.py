def CarpetFitting(width, length, price):
    grippers = 1 * width * 2 + length * 2
    carpetcost = width * length * price
    underlay = width * length * 3
    fitting = 50
    answer = carpetcost + grippers + underlay + fitting
    return answer



print("£",(CarpetFitting(7, 6, 17)))