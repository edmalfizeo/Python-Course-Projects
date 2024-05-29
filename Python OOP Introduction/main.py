import turtle
from turtle import *

timmy = Turtle()
my_screen = Screen()
timmy.shape('turtle')
timmy.color('darkolivegreen')

for i in range(20):
    timmy.forward(100)
    timmy.left(140)


my_screen.exitonclick()
