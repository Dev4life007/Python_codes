print("Hi guys,\n\nLet\'s solve for the sides of a right angled triangle using the program below.")
from math import *
Answer = input("What side are you solving for:\nHypotenuse?\nOpposite?\nAdjacent?  ")
if Answer == "Adjacent":
    b = float(input("Enter the length of opposite: "))
    c = float(input("Enter the length of hypotenuse: "))
    a_squared = (c**2) - (b**2) 
    a = round(sqrt(a_squared), 2)

    print("The length of the adjacent side is:", a,"cm")
    print("If you noticed, our answer was rounded to 2 decimal places to avoid too many decimals.")
    print("There you have it guys,\nwith this, all your pythagoras problems are solved.\nHope you had fun....\nCheers!")
elif Answer == "Opposite":
    c = float(input("Enter the length of hypotenuse: "))
    a = float(input("Enter the length of adjacent: "))
    b_squared = (c**2) - (a**2)
    b = round(sqrt(b_squared), 2)

    print("The length of the opposite side is:", b,"cm")
    print("If you noticed, our answer was rounded to 2 decimal places to avoid too many decimals.")
    print("There you have it guys,\nwith this, all your pythagoras problems are solved.\nHope you had fun....\nCheers!")
elif Answer == "Hypotenuse":
    b = float(input("Enter the length of opposite: "))
    a = float(input("Enter the length of adjacent: "))
    c_squared = (a**2) + (b**2)
    c = round(sqrt(c_squared), 2)

    print("The length of the hypotenuse side is:", c,"cm")
    print("If you noticed, our answer was rounded to 2 decimal places to avoid too many decimals.")
    print("There you have it guys,\nwith this, all your pythagoras problems are solved.\nHope you had fun...\nCheers!")
else:
    print("Try inputing the first letter in cap,\nIf it doesn\'t work,\nThen this program is not for you!")
