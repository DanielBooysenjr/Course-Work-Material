#Step 4

import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

lives = 6

print(hangman_art.logo)

#Create blanks
display = []

for _ in range(word_length):
    display += "_"

while '_' in display and lives > 0:

        guess = input("Guess a letter: ").lower()


        if guess in display:
            print(f"You already guessed the letter: {guess}")

        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
          print(f"The letter {guess} is not in the chosen word. You lose a live!")
          lives -= 1

        print(display)
        if "_" not in display:
            print("You win!")

        if lives == 0:
          print("\nYou Lose")

        print(hangman_art.stages[lives])