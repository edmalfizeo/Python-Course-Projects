from turtle import *
import random
turtle = Turtle()
screen = Screen()
directions = [0, 90, 180, 270]
turtle.pensize(8)
turtle.speed(10)
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomcolor = (r, g, b)
    return randomcolor


for i in range(1000):
    turtle.color(random_color())
    turtle.forward(30)
    turtle.left(random.choice(directions))




screen.exitonclick()