from random import *

def guess_number():
    valid = False
    int_valid = False
    n = randint(1,100)
    while valid == False:
        x = input("Guess an integer between 1 and 100: ")
        try:
            x = int(x)
            if x < n:
                print("Sorry, that number is too low.")
            if x > n:
                print("Sorry, that number is too high.")
            if x == n:
                print("Congratulations! You guessed the number!")
                valid = True
        except ValueError:
            print("Sorry, that is not an integer.")
            
guess_number()