# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

higest_score = 0

for current_score in student_scores:
    if current_score > higest_score:
        higest_score = current_score

print(higest_score)