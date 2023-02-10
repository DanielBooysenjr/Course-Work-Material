# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Check if year is divisable by 4
first4 = year % 4

# Check if year is divisable by 100
first100 = year % 100

# Check if year is divisable by 400
first400 = year % 400

if first4 == 0:
    print("Leap year.")
elif first100 >= 1:
    print("Not leap year.")
elif first100 >= 1 and first400 == 0:
    print("leap year.")
else:
    first4 >= 1
    print("Not leap year.")



