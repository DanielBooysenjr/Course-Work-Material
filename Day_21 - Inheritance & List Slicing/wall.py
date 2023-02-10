
# Creating a wall

from turtle import Turtle

x_cor = [300, 260, 220, 180, 140, 100, 60, 20, -20, -60, -100, -140, -180, -220, -260, -300]
y_cor = [300, 260, 220, 180, 140, 100, 60, 20, -20, -60, -100, -140, -180, -220, -260, -300]

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("red")

    def north_wall(self):
        for i in range(5):
            self.goto(x_cor[i], y_cor[i])