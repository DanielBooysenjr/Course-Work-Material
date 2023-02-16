
# The Great Squirrel Cencus Data Analysis (With Pandas)

import pandas as pd

# Read the .CSV File
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("Squirrel_Count.csv", index=False)

# primary_fur_color = (squirrel_data["Primary Fur Color"])

# black = []
# total_black = 0
# gray = []
# total_gray = 0
# cinnamon = []
# total_cinnamon = 0

# for colors in primary_fur_color:
#     if colors == "Gray":
#         gray.append(colors)
#     elif colors == "Black":
#         black.append(colors)
#     elif colors == "Cinnamon":
#         cinnamon.append(colors)

# for blacks in black:
#     total_black += 1

# for grays in gray:
#     total_gray += 1

# for cinnamons in cinnamon:
#     total_cinnamon += 1

# # Create new dictionary
# squirrel_dict = {
#         "black": [total_black],
#         "grey": [total_gray],
#         "cinnomon": [total_cinnamon]

# }

# print(squirrel_dict)

# squirrel_data = pandas.DataFrame(squirrel_dict)
# squirrel_data.to_csv("primary_fur_color.csv")