
# Hirst Spot Painting - Color Gram

# import colorgram
# import os

import turtle as turtle_module
import random

# os.chdir("C://Users//danie//Documents//Coding//100_Day_Python_Bootcamp//Intermediate//Day_18")

# rgb_colors = []
# colors = colorgram.extract('test.jpg', 6)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.hideturtle()
tim.speed(0)
tim.penup()

color_list = [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots +1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()