from random import *

def roll_dice():
    valid = False
    while valid ==False:
        n = randint(1, 6)
        print(n)
        x = input("Would you like to roll again? ")
        if x == "No":
            valid = True
    
roll_dice()