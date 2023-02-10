from art import *
from game_data import data
import random
from replit import clear

# Import logo & print greeting message

score = 0
# Get random integer from range of game_data - Data

# Store data in an empty dict
option_1 = {}
option_2 = {}
continue_game = True


def game():

    global score
    global continue_game

    print(logo)
    for i in data:
        # Get data from game data with the random integer value for option 1
        option_1_int = random.randrange(start=0, stop=49)
        option_1 = data[option_1_int]
        # Get data from game data with the random integer value for option 2
        option_2_int = random.randrange(start=0, stop=49)
        option_2 = data[option_2_int]
        # Make sure the same number can not be assigned to option 1 and 2
        if option_1_int == option_2_int:
            option_2_int = random.randrange(start=0, stop=49)

    print(option_1['name'])
    print(option_1['follower_count'])
    print(option_2['name'])
    print(option_2['follower_count'])


    # Print options
    print(
        f"Compare A: {option_1['name']}, {option_1['description']}, from {option_1['country']}\n"
    )
    print(vs)
    print(
        f"Against B: {option_2['name']}, {option_2['description']}, from {option_2['country']}\n"
    )

    follower_1 = [option_1['follower_count']]
    follower_2 = [option_2['follower_count']]

    # If followers are the same - Change the nums
    if follower_1 == follower_2:
        option_2_int = random.randrange(start=0, stop=49)
        option_2 = data[option_2_int]

    # Ask player to choose between option 1 and 2
    choice = input("Who has more followers? 'A' or 'B': ").lower()

    # Compare follower amount between option 1 and 2
    if choice == 'a' and follower_1 > follower_2:
        print("You won")
        score += 1
        clear()
        return print(f"Your Score is: {score}")
    elif choice == 'a' and follower_1 < follower_2:
        clear()
        print(f"Sorry, that's wrong. Final score was {score}")
        continue_game = False
    elif choice == 'b' and follower_2 > follower_1:
        print("You won")
        score += 1
        clear()
        return print(f"Your Score is: {score}")
    elif choice == 'b' and follower_2 < follower_1:
        clear()
        print(f"Sorry, that's wrong. Final score was {score}")
        continue_game = False


while continue_game == True:
    game()

