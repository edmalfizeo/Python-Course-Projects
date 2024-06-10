import random
from turtle import *

turtle = Turtle()
screen = Screen()
turtle.shape("turtle")
turtle.hideturtle()
screen.colormode(255)

colors_list = [(140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235), (209, 161, 111), (144, 29, 63),
               (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43), (195, 130, 169), (54, 168, 114),
               (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87), (193, 187, 46), (240, 204, 2),
               (1, 102, 119), (19, 22, 21), (50, 150, 109), (172, 212, 172), (118, 36, 34), (221, 173, 188),
               (227, 174, 166), (153, 205, 220), (184, 185, 210)]

turtle_position = [0, 0]


for i in range(10):
    turtle.penup()
    turtle.goto(turtle_position[0], turtle_position[1])
    turtle_position[1] += 40
    for j in range(10):
        turtle.dot(20, random.choice(colors_list))
        turtle.penup()
        turtle.forward(50)


screen.exitonclick()
