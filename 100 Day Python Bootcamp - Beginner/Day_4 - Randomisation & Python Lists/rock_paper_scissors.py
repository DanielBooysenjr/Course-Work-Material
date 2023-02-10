import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

choice_lower = choice.lower()

# Convert ASCII to list
opponent = [rock,paper,scissors]
          #  0      1       2

# Create random int from 0 - 2 (Choices)
random = random.randint(0,2)

# Allocate random number to opponent choice
opponent_choice = random


if choice == "0":
    print(rock)
    print("Computer Chose:")
    print(opponent_choice)
    if choice == "0" and opponent_choice == paper:
        print("You lose")
    elif choice == "0" and opponent_choice == rock:
        print("It is a draw")
    else:
        print("You win!")
elif choice == "1":
    print(paper)
    print("Computer Chose:")
    print(opponent_choice)
    if choice == "1" and opponent_choice == scissors:
        print("You lose")
    elif choice == "1" and opponent_choice == paper:
        print("It is a draw")
    else:
        print("You win")
elif choice == "2":
    print(scissors)
    print("Computer Chose:")
    print(opponent_choice)
    if choice == "2" and opponent_choice == scissors:
        print("It is a draw")
    elif choice == "2" and opponent_choice == rock:
        print("You lose")
    else:
        print("You win")
else:
    print("Invalid Selection")


if opponent_choice == "0":
    print(rock)
elif opponent_choice == "1":
    print(paper)
else:
    print(scissors)


