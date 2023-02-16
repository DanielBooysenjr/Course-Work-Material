#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


# Getting Names
with open("Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()


# Opening Starting Letter
with open("Input/Letters/starting_letter.txt", "r") as starting_letter:
    starting_letter_file = starting_letter.read()


# Writes the names to the new letter
for name in names:
    name = name.strip()
    new_letter = starting_letter_file.replace("[name]", name)
    # Saving letter to new file
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as latest:
        latest.write(new_letter)






# for name in names:
#     starting_letter = open("Input/Letters/starting_letter.txt")
#     new_letter = starting_letter.replace("[name]", name)
#     print(new_letter)





#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp