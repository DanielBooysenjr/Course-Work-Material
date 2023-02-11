
# Creating the cars class and generating random cars

from turtle import Turtle
import random

CAR_STARTING_POS_Y_AXIS = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]
COLORS = ["blue", "pink", "green", "purple", "red", "orange"]
PACES = 10


class CarGenerator:
    def __init__(self):
        self.all_cars = []
        self.car_speed = PACES


    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y_axis = random.choice(CAR_STARTING_POS_Y_AXIS)
            new_car.goto(x=300, y=random_y_axis)
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += PACES




