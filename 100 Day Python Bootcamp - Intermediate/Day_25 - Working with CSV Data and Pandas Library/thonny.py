# US States Game Using Pandas & Turtle

import turtle
import pandas
from turtle import Turtle


# Creating the window
screen = turtle.Screen()
screen.setup(width=725, height= 491)
screen.tracer()
screen.title("U.S States Quiz")

image = "blank_states_img.gif"

# Adding the background
turtle.addshape(image)
turtle.shape(image)

# Reading data from csv file
data = pandas.read_csv("50_states.csv")

# Cleaning up the Columb from spaces
states = data.state.str.strip()

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

# Getting Coor
row = (data[data.state == answer_state])
x = int(round(row["x"]))
y = int(round(row["y"]))
print(x)
print(y)


def place_text():
    text = Turtle()
    text.penup()
    text.hideturtle()
    text.write(answer_state)
    text.goto(x, y)


if answer_state in states.values:
    place_text()
else:
    print("Try Again")

game_is_on = True

while game_is_on:
    screen.update()




turtle.mainloop()

