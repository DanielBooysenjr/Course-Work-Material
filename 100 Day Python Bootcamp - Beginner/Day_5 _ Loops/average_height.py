# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# Add up the weights

counter = 0
for number in student_heights:
    counter += 1

# Add up the heights

total_height = 0

for total in student_heights:
    total_height += total


# Divide student heights by amount of students

average = total_height / counter

print(round(average))