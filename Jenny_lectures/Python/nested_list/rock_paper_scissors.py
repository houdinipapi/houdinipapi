#!/usr/bin/python3
"""
A rock, paper, and scissor game
"""

import random

user_choice = int(input("Pick a number: (0 - Rock, 1 - Paper, 2 - Scissor) "))
comp_choice = random.randint(0, 2)
print(f"The computer's choice is {comp_choice}")
print(f"Your choice is {user_choice}")

if user_choice < 0 or user_choice >= 3:
    print("PICK THE CORRECT NUMBER!!!")

else:
    if user_choice == comp_choice:
        print("It\'s a TIE!!")

    elif user_choice == 0 and comp_choice == 2:
        print("YOU WIN!!")

    elif user_choice == 2 and comp_choice == 0:
        print("COMP WINS!!!")

    elif user_choice > comp_choice:
        print("YOU WIN!!")

    elif comp_choice > user_choice:
        print("COMP WINS")
