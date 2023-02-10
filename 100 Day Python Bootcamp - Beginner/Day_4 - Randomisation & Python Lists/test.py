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


# Put options in list form
options = [rock, paper, scissors]

options_num = options

# Allocate numbers to list
options_lenth = len(options)

# Generate random number selection
random_choice = random.randrange(start=0, stop = options_lenth)


# Convert number back into variable (Image)
image = options

rock_image = options[0]
paper_image = options[1]
scissors_image = options[2]

opp_choices = [rock_image, paper_image, scissors_image]

# Computer chose
comp_chose = "\nComputer chose\n"

# print(rock_image)

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

choice_lower = player_choice.lower()


# Winning score
      
if choice_lower == "0":
    print(rock)
    print(comp_chose)
    if random_choice == 0:
        print(rock_image)
        print("Tie")
    elif random_choice == 1:
        print(paper_image)
        print("You lose")
    else:
        print(scissors_image)
        print("You win")

if choice_lower == "1":
    print(paper)
    print(comp_chose)
    if random_choice == 0:
        print(rock_image)
        print("You win")
    elif random_choice == 1:
        print(paper_image)
        print("Tie")
    else:
        print(scissors_image)
        print("You lose")
if choice_lower == "2":
    print(scissors)
    print(comp_chose)
    if random_choice == 0:
        print(rock_image)
        print("You lose")
    elif random_choice == 1:
        print(paper_image)
        print("You win")
    else:
        print(scissors_image)
        print("Tie")