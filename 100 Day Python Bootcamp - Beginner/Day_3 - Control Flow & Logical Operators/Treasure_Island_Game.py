
# Zombie type based game - The walking Goo

print('''              ,
          _,-""-._
        ,"        ".
       /    ,-,  ,"\
      "    /   \ | o|
      \    `-o-"  `-',
       `,   _.--'`'--`
         `--`---'                    |   _)
           ,' '      _  /  _ \  ` \   _ \ |  -_)
         ./ ,  `,    ___|\___/_|_|_|_.__/_|\___|
         / /     \
        (_)))_ _,"
           _))))_,
  --------(_,-._)))-------------------------------''')

  # Welcome texts

print("Welcome to Treasure Island.\n")
print("I am the dungeon master, Loruko!\n")
print("Your mission is to find the treasure, But be careful, danger lurkes around these parts of the world!")
print("You have been warned, mortal")

# Game

choice_1 = input("You wake up in an abanadoned basement, after thte start of a global zombie apocolypse!\nYou see a door to the left and a door to the right, which do you choose?\nType: left or right ")
choice_1_lower = choice_1.lower()

if choice_1_lower == "left":
    print("\nYou open the door to the left and see an exit sign! You quickly run out and find yourself in a deserted world!\n")
    print("\nYou have two options, either run for your life down the streets, or head into the forest!")
    choice_2 = input("Type: Head down the street or head into the forest ")
    choice_2_lower = choice_2.lower()
    if choice_2_lower == "head into the forest":
        print("You find a safe place to set up camp for the night and to gather yourself!")
        print("\n You set up camp and spend the night, in the morning you can either go back into town, or head deeper into the forest.\n")
        choice_3 = input("Type: Head deeper into the forest or Go back into town. ")
        choice_3_lower = choice_3.lower()
        if choice_3_lower == "go back into town":
            print("\nYou find a general store, full of equipment!\n")
            print("You equip yourself with weapons, food and water! Now you are ready!\n")
            print("You have two options, go back outside and head east or west!\n")
            choice_4 = input("Type: Go east or Go West ")
            choice_4_lower = choice_4.lower()
            if choice_4_lower == "go east":
                print("You head east into a small town, where most of everything still seems in tact!\n")
                print("You see a house on the left, a farm on the right and a car further down the street, which do you choose?\n")
                choice_5 = input("type: House, Farm or Car ")
                choice_5_lower = choice_5.lower()
                if choice_5_lower == "farm":
                    print("You are attacked by hillbilly farmers, you died! Game Over!")
                elif choice_5_lower == "car":
                    print("You find your way out of the mess, back to safety! You win the game!")
                elif choice_5_lower == "house":
                    print("You are attached by an angry family. Game Over!")
                else:
                    print("Wrong input. Game Over!")

            else:
                print("You are swarmed by a horde of Zombies! Game Over! ")

        else:
            print("You venture to far into the forest, and get attacked by wild animals. Game Over!")
    else:
        print("You are attacked by a horde of Zombies! Game Over")
else:
    print("Game Over!")
    
