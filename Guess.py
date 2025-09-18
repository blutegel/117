"""
Lab 1
Group #NA

Author: James Rohr
Date: 9-25-25

This game will have the function generate a random number
 between 1-100 and give the user 5 predefined number of tries
 to guess the number"""

import random

def guess_game():
    random_number = random.randint(1, 100)
    count = 5
    print("You have 5 guesses to guess my secret number between 1-100.")

    while count > 0:
        Users_Guess = int(input("Enter a number between (1-100): "))

        if Users_Guess == random_number:
            print("You guessed my secret number!")
            return
        elif Users_Guess > random_number:
            print("Your guess is too high!")
        else:
            print("Your guess is too low!")
        count -= 1
        print(f"You have {count} {("guesses", "guess")[count==1]} left. Try again!")

    print(f"Sorry, you are out of guesses. The secret number was {random_number}.")
