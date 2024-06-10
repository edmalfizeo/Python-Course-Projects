from turtle import *
import random
turtle = Turtle()
screen = Screen()
directions = [0, 90, 180, 270]
turtle.speed(100)
screen.colormode(255)

r = 100


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomcolor = (r, g, b)
    return randomcolor


for i in range(80):
    turtle.color(random_color())
    turtle.circle(r)
    turtle.left(5)

screen.exitonclick()