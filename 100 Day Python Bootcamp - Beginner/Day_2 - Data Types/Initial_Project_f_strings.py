
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
total_bill = input('What is the total bill? ')
bill_split = input('How many people to split te bill? ')
bill_percentage = input('What percentage tip would you like to give? 10, 12 or 15? ')

# Divide the bill with the total people to get the amount each person should pay

divided = (f"{total_bill}" / f"{bill_split}")

# Convert all inputs to integers

bill = int(total_bill)
split = int(bill_split)
percentage = int(bill_percentage)


# Divide the bill with the total people to get the amount each person should pay

each_person_to_pay = bill / split

# Convert tip to percentage

percentage_payable = (percentage / bill) * 100 / 2

# Adding it together

bill_due = each_person_to_pay + percentage_payable
print(divided)