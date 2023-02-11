
# Creating the turtle class

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        
        self.shape("turtle")
        self.color("black")
        self.penup()

    def move_to_start(self):
        self.setheading(90)
        self.goto(x=0, y=-280)

    def move_forward(self):
        self.forward(20)