
# Blackjack Game

import random
from logo import logo

start_game = input("Would you like to start a game of Blackjack? Type 'Y' to start: ").lower()

if start_game == "y":
    print(logo)
    print("Welcome to the Blackjack game!")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start_game = True

player_hand = random.choices(cards,k=2)
if sum(player_hand) == 21:
        start_game = False           
        print(f"Your total is {sum(player_hand)} You win!")
computer_hand = random.choices(cards,k=2)

player_totals = []
computer_totals = []

print(f"Your cards are: {player_hand}, your total is: {sum(player_hand)}\n")
print(f"The computers first card is: {computer_hand[0]}\n")


def over_max():
    '''Check whether the totals are over 21'''
    global start_game
    player_totals = sum(player_hand)
    if player_totals > 21:
        print(f"Your final hand was {player_hand}, total {player_totals}.\n")
        print("You lose!")
        start_game = False
    else:
        start_game = True

def winner():
    global start_game
    player_totals = sum(player_hand)
    computer_totals = sum(computer_hand)

    if player_totals < 21 and player_totals > computer_totals:
        print(f"Your final hand was {player_hand}, your total was {player_totals}")
        print(f"The computer hand was {computer_hand}, it's total was {computer_totals}")
        print("You win!")
        start_game = False
    elif player_totals == 21:
        print(f"Your total is {player_totals} You win!")
        start_game = False
    elif computer_totals == 21:
        print(f"Computer total is {computer_totals}, You lose!")
        start_game = False
    elif player_totals == computer_totals:
        print(f"It's a draw, both have {player_totals}")
        start_game = False
    else:
        print(f"Your final hand was {player_hand}, your total was {player_totals}")
        print(f"The computer hand was {computer_hand}, it's total was {computer_totals}")
        print("You lose!")
        start_game = False

def scores():
    print(f"Your current hand is {player_hand} your total is {sum(player_hand)}\n")
    print(f"The computer's first card is {computer_hand[0]}\n")


while start_game == True:
    another_card = input("Type 'Y' to get another card, type 'n' to pass: ")
    if another_card == "y":
        new_card = random.choice(cards)
        if new_card == cards[0] and sum(player_hand) < 21:
            ace = int(input("You got an ace, would you like '1' or '11'? "))
            if ace == 1:
                new_card = 1
                player_hand.append(new_card)
            else:
                new_card = 11
                player_hand.append(new_card)
        else:
            player_hand.append(new_card)
            winner()
    elif player_totals == 21:
        print(f"Your total is {player_totals} You win!")
        start_game = False        
        if sum(computer_hand) < 17:
            computer_hand.append(random.choice(cards))
        over_max()
        if start_game == True:
            scores()
    else:
        start_game = False
        winner()