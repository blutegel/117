"""
Lab 1
Group #NA

Author: James Rohr
Date: 9-25-25

This main file allows the user to choose between two games.  First game is a random number
guessing game, and the second game is rock paper scissors"""

from Guess import guess_game
from rock_paper_scissors import rockpaperscissors_game


def main():
    playing = True

    while playing:
        user_selection = int(input("Enter your choice: \n"
                                   "1. Random Number Guessing Game\n"
                                   "2. Rock Paper Scissors Game\n"
                                   "3. Exit\n"))

        if user_selection == 1:
            guess_game()
        elif user_selection == 2:
            rockpaperscissors_game()
            pass
        elif user_selection == 3:
            print("Thank you for playing!")
            playing = False
        else:
            print("You chose an invalid option.")


if __name__ == "__main__":
    main()
