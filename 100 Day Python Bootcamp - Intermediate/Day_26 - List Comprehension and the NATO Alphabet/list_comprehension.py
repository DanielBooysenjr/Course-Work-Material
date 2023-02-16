# # List Comprehension

# numbers = [1, 2, 3]
# new_numbers = [n + 10 for n in numbers]
# print(new_numbers)

# name = "Daniel"
# new_list = [letter for letter in name]
# print(new_list) 

# numbers = range(1, 5)
# new_numbers = [num *2 for num in numbers]
# print(new_numbers)

# new_nums = [num * 2 for num in range(1, 5)]
# print(new_nums)

# # Conditional List Comprehension

# names = ["Alex", "Beth", "Dave", "Eleanor", "Freddie", "Caroline"]
# short_names = [name for name in names if len(name) > 5]
# print(short_names)

# names = ["Alex", "Beth", "Dave", "Eleanor", "Freddie", "Caroline"]
# capitalized_long_names = [name.upper() for name in names if len(name) > 5]
# print(capitalized_long_names)