#!/bin/python3

import random
guess = 12

#the user can guess for a number between one and nine, end the game anywhere typing "exit"
while True and guess!= "exit":
    i=1
    ran = random.randint(1,9)
    if guess == "exit":
        break
    else:
        while int(guess) != ran and guess !="exit":
            guess = input("guess a number between 1 and 9 (including both)!\n")
            if guess == "exit":
                break
            elif int(guess) == ran:
                print("you guessed correct! Tries: " +str(i))
            elif int(guess) < ran:
                print("you guessed too low")
                i +=1
            elif int(guess) > ran:
                print("you guessed too high")
                i +=1
