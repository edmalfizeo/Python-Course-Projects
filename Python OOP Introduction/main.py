import random
from turtle import *
import random

timmy = Turtle()
my_screen = Screen()
timmy.shape('turtle')
timmy.color('darkolivegreen')
timmy.speed(10)
timmy.setpos(0, 0)
my_screen.setup(width=800, height=600)

for i in range(1000):
    timmy.pencolor(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))

    timmy.pensize(random.randint(1, 5))

    side = random.randint(1, 200)

    for j in range(5):
        if timmy.xcor() >= 401:
            timmy.penup()
            timmy.goto(-400, timmy.ycor())
            timmy.pendown()
        if timmy.ycor() >= 300:
            timmy.penup()
            timmy.goto(timmy.xcor(), -300)
            timmy.pendown()
        timmy.forward(side)
        timmy.left(120)
        timmy.forward(side)
        timmy.right(120)

my_screen.exitonclick()
