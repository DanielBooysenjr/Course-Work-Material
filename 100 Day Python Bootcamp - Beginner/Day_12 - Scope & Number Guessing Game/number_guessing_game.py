
# Number Guessing Game

import random
from logo import logo

def game():

    # Defining global variables
    lives = 0
    dificulty = ''

    # Game Start
    random_num = random.randrange(start = 1, stop = 100)
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number betwen 1 and 100.")

    dificulty = input("Choose a dificulty. Type 'easy' or 'hard': ").lower()

    if dificulty == "hard":
        lives = 5
    elif dificulty == "easy":
        lives = 10

    print(f"You chose {dificulty}, you have {lives} lives in total.\n")

    while lives > 0:
        make_guess = int(input("Choose your guess: "))
        if make_guess > 100:
            print("Please guess within the range of 1 and 100")
        elif make_guess > random_num:
            print(f"You chose {make_guess}, go lower")
            lives -= 1
            if lives > 0:
                print(f"Wrong choice, you have {lives} lives remaining")
            else:
                print("You ran out of guesses. You lose")
        elif make_guess < random_num:
            print(f"You chose {make_guess}, go higher")
            lives -= 1
            if lives > 0:
                print(f"Wrong choice, you have {lives} lives remaining")
            else:
                print("You ran out of guesses. You lose")
        elif make_guess == random_num:
            print("You Won!")
            lives = 0
    
    restart = input("Would you like to restart? Type 'Yes' or 'No': ")
    if restart == 'yes':
        lives = lives
        game()

game()