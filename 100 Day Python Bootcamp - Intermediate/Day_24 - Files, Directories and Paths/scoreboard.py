
# Scoreboard

from turtle import Turtle
import os

os.chdir("C:\\Users\\danie\\Documents\\Coding\\100_Day_Python_Bootcamp\\100 Day Python Bootcamp - Intermediate\\Day_24 - Files, Directories and Paths")


ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_scores.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=-10, y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Your score is: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_scores.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
        

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)


    def increase_score(self):   
        self.score += 1
        self.update_scoreboard()


