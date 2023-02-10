#Step 3

import random



stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      | 
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while '_' in display and lives > 0:

        guess = input("Guess a letter: ").lower()

        #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
          #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
          lives -= 1

        print(display)
        if "_" not in display:
            print("You win!")

        if lives == 0:
          print("\nYou Lose")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
        print(stages[lives])