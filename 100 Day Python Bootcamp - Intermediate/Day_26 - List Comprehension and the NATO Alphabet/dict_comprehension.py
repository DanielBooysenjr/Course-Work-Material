# # List Comprehension Using Dict

import random

names = ["Alex", "Beth", "Dave", "Eleanor", "Freddie", "Caroline"]

student_scores = {student:random.randint(1,101) for student in names}

# print(student_scores)

passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}

print(passed_students)