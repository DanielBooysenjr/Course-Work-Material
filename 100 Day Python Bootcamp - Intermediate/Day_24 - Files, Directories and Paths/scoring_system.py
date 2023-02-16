
import os

# Opening .txt files

# os.chdir("C:\\Users\\danie\\Documents\\Coding\\100_Day_Python_Bootcamp\\100 Day Python Bootcamp - Intermediate\\Day_24 - Files, Directories and Paths")

# Reading a file
with open("high_scores.txt") as file:
    contents = file.read()
    print(contents)

# Writing to file
with open("high_scores.txt", mode="w") as file:
    file.write("\nNew Text.")
