#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲

import random
	 
#Write the rest of your code below this line 👇

random = random.randint(0,1)

if random == 0:
    print("Heads")
elif random == 1:
    print("Tails")