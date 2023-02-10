
# Pong Game

# # Import neccesary libraries - Tutrtle, Time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



# # Create window
    # Create Turtle instances of Turtle class to draw center of screen line

screen = Screen()
screen.setup(width=800, height=600, startx=350, starty=100,)
screen.bgcolor("black")
screen.title("Classic Arcade Pong Game")
# Removing animation
screen.tracer(0)



# # Create turtle instances - Opponent and player - Sep. Class
# Right paddle & Left paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# # Create ball

ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


# # Set up screenboard - Sep. Class


# # Detect Collision with ball
    # Make ball move back in opposite direction


# # Detect collision with screen edge - Game Over

game_is_on = True

while game_is_on:
    # Updating screen
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Check if ball collided with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Ball needs to bounce
        ball.bounce_y()

    # Detect collision with right and left paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when left paddle misses
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()