# How to iterate over a Pandas Dataframe

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)


# # Loop through DataFrame

# for (key, value) in student_dataframe.items():
#     print(value)

# Loop through rows of data using Pandas
for (index, row) in student_dataframe.iterrows():
    if row.student == "Angela":
        print(row.score)