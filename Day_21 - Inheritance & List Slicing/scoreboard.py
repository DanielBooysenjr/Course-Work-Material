
# Scoreboard

from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_scores = {}
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=-10, y=270)
        self.update_scoreboard()


        
    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.write(f"Your score is: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):   
        self.score += 1
        self.clear()
        self.update_scoreboard()


