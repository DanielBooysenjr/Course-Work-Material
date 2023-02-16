# Working with CSV Data and Pandas Lib

# Importing Libraries
import csv
import pandas

# Importing the CSV File

with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

# Importing the CSV file with CSV library
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    # Creating new list of just temperatures
    temperatures = []   
    # Looping through the data, to display it
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
        # print(row)
    print(temperatures)

# Using Panda Library

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()

# Getting Average Temp
print(data["temp"].mean())

# Getting Max Temp
print(data["temp"].max())

# Another way of getting a columb information
print(data.condition)

# Getting row data
print(data[data.day == "Monday"])

# Getting max temp and print row
max = data.temp.max()
print(data[data.temp == max])

# Anotherway of getting max temp and printing row
print(data[data.temp == data.temp.max()])

# Converting Monday's temp from C to F
monday = data[data.day == "Monday"]
celcius = int(monday.temp)
fahrenheit = (celcius * 9/5) + 32
print(fahrenheit)

# Create dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]

            }

data = pandas.DataFrame(data_dict)
# Saving DF to new file
data.to_csv("new_data.csv")


