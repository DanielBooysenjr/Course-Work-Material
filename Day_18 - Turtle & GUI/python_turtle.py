
# Python Turtle

import turtle as t
from turtle import Screen
import random

shelly_the_turtle = t.Turtle()
t.colormode(255)

# shelly_the_turtle.shape("turtle")
# shelly_the_turtle.color("navyblue")

# # Draw a square with Shelly

# for movement in range(4):
#     shelly_the_turtle.forward(100)
#     shelly_the_turtle.left(90)

# shelly_the_turtle.forward(100)
# shelly_the_turtle.left(90)
# shelly_the_turtle.forward(100)
# shelly_the_turtle.left(90)
# shelly_the_turtle.forward(100)
# shelly_the_turtle.left(90)

# # Draw a striped line with Shelly

# for movement in range(15):
#     shelly_the_turtle.forward(10)
#     shelly_the_turtle.penup()
#     shelly_the_turtle.forward(10)
#     shelly_the_turtle.pendown()


# Drawing different shapes

# for triangle in range(3):
#     shelly_the_turtle.right(120)
#     shelly_the_turtle.forward(100)

# for square in range(4):
#     shelly_the_turtle.right(90)
#     shelly_the_turtle.forward(100)

# for pentagon in range(5):
#     shelly_the_turtle.right(72)
#     shelly_the_turtle.forward(100)

# for hexagon in range(6):
#     shelly_the_turtle.right(60)
#     shelly_the_turtle.forward(100)

# for octagon in range(8):
#     shelly_the_turtle.right(45)
#     shelly_the_turtle.forward(100)

# for nonagon in range(9):
#     shelly_the_turtle.right(40)
#     shelly_the_turtle.forward(100)

# for decacon in range(10):
#     shelly_the_turtle.right(36)
#     shelly_the_turtle.forward(100)

# # Optemized code:

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         shelly_the_turtle.forward(100)
#         shelly_the_turtle.right(angle)

# for shape_side in range(3,11):
#     draw_shape(shape_side)


# # Let Shelly take a random walk always moving 50 paces but in a random direction and each time it changes direction it changes color.

# direction = [0, 90, 180, 270]
# colors = ['red', 'green', 'blue', 'cyan', 'lightgreen', 'turquoise', 'skyblue']
# sizes = [1, 2, 3, 4, 5]
# speeds = [0, 10, 6, 3, 1]

# for rand in range(2000):
#     shelly_the_turtle.forward(50)
#     shelly_the_turtle.color(random.choice(colors))
#     shelly_the_turtle.speed(random.choice(speeds))
#     shelly_the_turtle.pensize(random.choice(sizes))
#     shelly_the_turtle.right(random.choice(direction))


# # Generate a different color in the RGB range

# direction = [0, 90, 180, 270]
# sizes = [1, 2, 3, 4, 5]
# speeds = [0, 10, 6, 3, 1]


# for rand in range(2000):
#     shelly_the_turtle.forward(50)
#     shelly_the_turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
#     shelly_the_turtle.speed(random.choice(speeds))
#     shelly_the_turtle.pensize(random.choice(sizes))
#     shelly_the_turtle.right(random.choice(direction))















# draw_lines(colors)



# Keep this code at the bottom 

screen = Screen()
screen.exitonclick()