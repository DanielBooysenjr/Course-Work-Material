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

# Moving the text to the correct pos
def place_text():   
    text = Turtle()
    text.penup()
    text.hideturtle()
    text.goto(x, y)
    text.write(answer_state)


guess = 0

game_is_on = True

while game_is_on:

    answer_state = screen.textinput(title=f"Guess the State. {guess}/50", 
    prompt="What's another state's name?").title()

    if answer_state in states.values:
        guess += 1
        # Getting Coor 
        row = (data[data.state == answer_state])
        x = int(round(row["x"]))
        y = int(round(row["y"]))
        # Placing text on screen
        place_text()

    # Checking what to do if user is incorrect
    elif answer_state not in states.values:
        print("Try Again")

    screen.update()


turtle.mainloop()