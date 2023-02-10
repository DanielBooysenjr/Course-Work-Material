
tall = (int(input("How tall are you in cm? ")))

if tall >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age >= 12 < 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("You are not tall enough to ride the.")