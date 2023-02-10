import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

# Create empty Variables
final_letters = ""
final_symbols = ""
final_numbers = ""

letters 
for random_letter in range(nr_letters):
    rand = str(random.choice(letters))
    final_letters += rand

# Generate random symbols
for random_symbol in range(nr_symbols):
    rand = str(random.choice(symbols))
    final_symbols += rand

# Generate random numbers
for random_number in range(nr_numbers):
    rand = str(random.choice(numbers))
    final_numbers += rand

# Add the randomness together
added = final_letters + final_symbols + final_numbers

# Making it easier
password = added

# Shuffle the password
final_password = ''.join(random.sample(password,len(password)))

# Print the password
print(f"Your password is: {final_password}")




