
# Creating a wall

from turtle import Turtle, Screen

scr = Screen()
scr.addshape("wall.gif")


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pensize(width=38)
        self.color("brown")
        self.goto(x=290, y=290)
        self.pendown()
        self.goto(x=-290, y=290)
        self.goto(x=-290, y=-290)
        self.goto(x=290, y=-290)
        self.goto(x=290, y=290)

