#!/bin/python3
a = ["Rock", "Paper", "Scissors"]

while len(a) > 0:
    p1 = input("Player 1, please make your choice! \n Rock, Paper or Scissors?\n\n")
    p2 = input("\nPlayer 2, please make your choice! \n Rock, Paper or Scissors?\n\n")

    if (p1 in a) == False:
        print("Player 1: your command was unknown to the game")
    elif (p2 in a) == False:
        print("Player 2: your command was unknown to the game")
    elif p1 == p2:
        print("\nIt's a draw!\n")
    elif (p1 == "Paper") & (p2 == "Rock"):
        print("\nPlayer 1 wins!\n")
    elif (p1 == "Paper") & (p2 == "Scissors"):
        print("\nPlayer 2 wins!\n")
    elif (p1 == "Rock") & (p2 == "Paper"):
        print("\nPlayer 2 wins!\n")
    elif (p1 == "Rock") & (p2 == "Scissors"):
        print("\nPlayer 1 wins!\n")
    elif (p1 == "Scissors") & (p2 == "Paper"):
        print("\nPlayer 1 wins!\n")
    elif (p1 == "Scissors") & (p2 == "Rock"):
        print("\nPlayer 2 wins!\n")


    usr_command = input("\nWish to continue? Enter / press N \n")

    if usr_command == "n":
        break
