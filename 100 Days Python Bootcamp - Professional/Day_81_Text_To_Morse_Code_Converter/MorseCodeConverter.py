
# Text to morse code converter

# Morse Code Alphabet

Alphabet = {
    'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ', 'E': '. ', 'F': '..-. ', 'G': '--. ', 'H': '.... ',
    'I': '.. ', 'J': '.--- ', 'K': '-.- ', 'L': '.-.. ', 'M': '-- ', 'N': '-. ', 'O': '--- ', 'P': '.--. ',
    'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ', 'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ',
    'Y': '-.-- ', 'Z': '--.. ', '0': '----- ', '1': '.---- ', '2': '..--- ', '3': '...-- ', '4': '....- ',
    '5': '..... ', '6': '-.... ', '7': '--... ', '8': '---.. ', '9': '----. ', ' ': '/ ', '.': '.-.-.- ',
    ',': '--..-- ', '?': '..--.. ',
}

def morse_code_converter():
    morse_code = True
    while morse_code:
        # start = input("Please type what").lower()
        text_input = input("What would you like to encrypt? ").upper()
        text_output = ""
        for l in text_input:
            if l in Alphabet:
                text_output += Alphabet[l]
        print(f'The encrypted morse code is:\n{text_output}')
        del text_output
        redo = input('Would you like to do another? Type "y" for yes or "n" for no: ')
        if redo == 'n':
            morse_code = False
            print("Bye Bye")
        
morse_code_converter()
