
# Turtle Crossing The Road

from turtle import  Screen
from player import Player
from car_generator import CarGenerator
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing The Road")
screen.tracer(0)
screen.listen()

# Creating Player Instance
player = Player()
car = CarGenerator()
scoreboard = Scoreboard()

# Moving Player
screen.onkeypress(player.move_forward, "Up")
player.move_to_start()

# Generate cars

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    # Move car across screen
    car.generate_car()
    car.move_cars()

    # Detect collision with car
    for i in car.all_cars:
        if i.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect if turtle crossed
    if player.ycor() > 290:
        player.move_to_start()
        scoreboard.level_up()
        car.level_up()
            


screen.exitonclick()

            






