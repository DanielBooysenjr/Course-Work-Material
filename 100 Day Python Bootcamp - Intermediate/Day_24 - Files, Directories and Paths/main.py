
# new_segment Game

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from wall import Wall
import time



screen = Screen()
# screen.bgpic("background.gif")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nokia 3310 Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
wall = Wall()
scoreboard = Scoreboard()

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


# # Detect collision with food
    # # If collision detected, increase size of new_segment, respawn food randomly on x,y coordinates and add to score
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


# # Detect colision with wall - Game Over

    if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
        scoreboard.reset()
        snake.reset()
        


# # Detect colision with body - Game Over
    # If head collides with any segment in the tail:
        # Trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 1:
            scoreboard.reset()
            snake.reset()

# # Stops the food to respawn on top op the snake
    for segment in snake.segments:
        if segment.distance(food) < 10:
            food.refresh()




screen.exitonclick()