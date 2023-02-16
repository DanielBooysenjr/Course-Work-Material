# Data Overlap, List Comprehension with multiple files

# # Localhost Test

file_1 = open("file1.txt")
first = file_1.readlines()

file_2 = open("file2.txt")
second = file_2.readlines()

result = [int(num.strip()) for num in first and second if num == num]


# Write your code above 👆

print(result)

# # Coding Rooms Test

# with open("file1.txt") as file1:
#     file_1_data = file1.readlines()
# with open("file2.txt") as file2:
#     file_2_data = file2.readlines()

# result = [int(num) for num in file_1_data if num in file_2_data]

# print(result)


