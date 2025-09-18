"""
Lab 1
Group #NA

Author: James Rohr
Date: 9-25-25

A guessing game with rock, paper, scissors is a game where you choose a random number between 1 and 3
corresponding to one of the items.  The computer make a random number between 1 and 3 to choose their item.  The items
are then compared to see who wins the round, specifically, rock defeats scissors, paper defeats rock, and scissors defeat paper.
"""

import random

def rockpaperscissors_game():
    computer_item = random.randint(1, 3)
    user_item = int(input("Select the item you want to use:\n" \
                         "1. Rock\n" \
                         "2. Paper\n" \
                         "3. Scissors\n"))

    print(f"You have chosen the item: {item_text(user_item)}")
    print(f"The computer has chosen their item to be: {item_text(computer_item)}")

    result = determine_outcome(user_item, computer_item)
    print(result)

def determine_outcome(user_item, computer_item):
    if user_item == computer_item:
        return "It's a tie!"
    elif (user_item == 1 and computer_item == 3) or \
         (user_item == 2 and computer_item == 1) or \
         (user_item == 3 and computer_item == 2):
        return "Congratulations, you win!"
    else:
        return f"Sorry, you lose. Since {item_text(computer_item)} beats {item_text(user_item)}."

def item_text(i):
    if i == 1:
        return "Rock"
    elif i == 2:
        return "Paper"
    elif i == 3:
        return "Scissors"
    else:
        return "Invalid choice, please select a number between 1 and 3."