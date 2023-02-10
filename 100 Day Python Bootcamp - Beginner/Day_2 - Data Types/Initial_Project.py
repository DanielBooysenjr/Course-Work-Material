print("Welcome to the tip calculator.")
total_bill = input('What is the total bill? ')
bill_split = input('How many people to split te bill? ')
bill_percentage = input('What percentage tip would you like to give? 10, 12 or 15? ')


# Convert total bill, bill split and bill percentage to integer

bill = int(total_bill)
split = int(bill_split)
percentage = int(bill_percentage)

# Divide the total bill amount with the amount of people

eachPerson = bill / split

# Work out how much each person should pay

pay = round(eachPerson / percentage,2)

print(pay)