
# Caesar Cipher Encryption - Part 1

import logo

print(logo.logos)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def restart():
    restart =  input("Would you like to restart the cipher program? 'Yes' or 'No' ").lower()

    while restart == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction,text,shift)
            

def caesar(direction, text, shift):

    new_word = ""
    index = ''
    
    if direction == "encode":
        for letter in text:
            if letter in alphabet:
                index = alphabet.index(letter)
                new_shift = index + (shift % 26)
                new_letter = alphabet[new_shift]
                new_word += new_letter
            else:
                new_word += letter

        print(f"the ecoded text is: {new_word}")


    if direction == "decode":
        for letter in text:
            if letter in alphabet:
                index = alphabet.index(letter)
                new_shift = index - (shift % 26)
                new_letter = alphabet[new_shift]
                new_word += new_letter
            else:
                new_word += letter

        print(f"the ecoded text is: {new_word}")

caesar(direction, text, shift)
restart()



