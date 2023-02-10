
# Turtle Race Game

from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Turtle betting game", prompt="Bet on which Turtle will win, enter a color: ")
print(user_bet)

colors = ["Red", "Blue", "Green", "Purple", "Orange", "Yellow"]
y_positions = [-70, -40, -10, 20, 50, 70]
all_turtles = []


for random_turtle in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[random_turtle])
    new_turtle.goto(x=-230, y=y_positions[random_turtle])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color} is the winner!")
            else:
                print(f"You've lost!! {winning_color} is the winner!")

        random_paces = random.randint(0,10)
        turtle.forward(random_paces)



screen.exitonclick()
