
fizz = "Fizz"
buzz = "Buzz"
fizzbuzz = "FizzBuzz"

for current_number in range(1,101):
    if current_number % 3 == 0 and current_number % 5 == 0:
        current_number = fizzbuzz
        print(current_number)
    elif current_number % 3 == 0:
        current_number = fizz
        print(current_number)
    elif current_number % 5 == 0:
        current_number = buzz
        print(current_number)
    else:
        print(current_number)

