
# Day 19
    # Higher order functions
    # Creating sketching game with Turtle

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Use functions as inputs:

def move_formwards():
    tim.forward(10)

def turn_right():
    tim.right(18)

def turn_left():
    tim.left(18)

def backwards():
    tim.back(10)

def clear_screen():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_formwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="c", fun=clear_screen)



screen.exitonclick()