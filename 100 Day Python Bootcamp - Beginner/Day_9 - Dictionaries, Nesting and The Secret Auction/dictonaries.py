
# Python Dictonaries

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

# Calls the specific key in the dictionary. Prints the Value
# print(programming_dictionary["Bug"])

# Adding new items to the dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again."

# print(programming_dictionary)

# Create an empty dictionary

empty_dictionary = {}

# Wipe an existing dictionary

# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary

programming_dictionary["Bug"] = "Moth in your computer"
print(programming_dictionary)

# Loop through a dictionary

for key in programming_dictionary:
    # Below line prints the key of the dictionary
    print(key)
    # Below line will print the value of the key. Key is not a pythonic statement. Should be the same as in the for loop
    print(programming_dictionary[key])