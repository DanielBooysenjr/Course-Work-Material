
# new_segment Game

from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nokia 3310 new_segment Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


# #  Move new_segment forward





# # Control new_segment with arrows





# # Detect collision with food
    # # If collision detected, increase size of new_segment, respawn food randomly on x,y coordinates and add to score





# # Detect colision with wall - Game Over





# # Detect colision with body - Game Over



screen.exitonclick()