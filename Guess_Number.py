# Guess the Number Game

import random

x = random.randint(1, 20)
guess = input("Guess a number between 1 and 20: ")

while guess.isnumeric() == True:
    if x > int(guess):
        print("Number is to low!")
        guess = input("Guess Again: ")
    elif x < int(guess):
        print("Number is to high!")
        guess = input("Guess Again: ")
    else:
        print("YOU GUESSED IT!!")
        break








