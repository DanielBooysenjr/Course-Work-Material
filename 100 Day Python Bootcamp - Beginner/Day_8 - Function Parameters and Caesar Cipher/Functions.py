
# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

'''
def greet():
    print("This is the greet function")
    print("Daniel Booysen was the programmer")
    print("Daniel Booysen will be the best Python programmer!")

greet()
'''
# Function that allows for input

'''def greet_with_name(name):
    print(f"This is the {name} function")
    print(f"{name} was the programmer")

greet_with_name("Daniel")'''

# Functions with more than 1 input

'''def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Daniel", "Portugal")'''

# Positional arguments

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with(location = "Portugal", name = "Daniel")