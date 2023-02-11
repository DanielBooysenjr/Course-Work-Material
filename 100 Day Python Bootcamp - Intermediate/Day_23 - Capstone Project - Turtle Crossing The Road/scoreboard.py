# Scoreboard

from turtle import Turtle

level_pos = (-270, 270)
game_over_pos = (0, 0)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(level_pos)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(game_over_pos)
        self.write("Game Over", align="center", font=("Courier", 20, "normal"))

    def level_up(self):
        self.level += 1
        self.update_scoreboard()
