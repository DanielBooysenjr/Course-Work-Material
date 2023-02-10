
# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Check Lenth


lenth = len(names)

random_name = (names[random.randrange(start=0,stop=lenth)])

print(f"{random_name} is going to buy the meal today! ")


