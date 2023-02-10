import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

random_letters = []
random_numbers = []
random_symbols = []

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

for random_letter in range(nr_letters):
    rand = str(random.choice(letters))
    random_letter = rand
    random_letters.append(rand)
print(random_letters)


for random_symbol in range(nr_symbols):
    rand = str(random.choice(symbols))
    random_symbol = rand
    random_symbols.append(rand)
print(random_symbols)

for random_number in range(nr_numbers):
    rand = str(random.choice(numbers))
    random_number = rand
    random_numbers.append(rand)
print(random_numbers)

combined = str(random_letters + random_symbols + random_numbers)













# print(f"Your password is {password}")