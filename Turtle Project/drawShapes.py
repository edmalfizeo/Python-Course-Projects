from turtle import *
import random
turtle = Turtle()
turtle.shape('turtle')
turtle.color('darkgreen')
turtle.pensize(1)

# Main

def draw_shapes(num_sizes):
    angles = 360 / num_sizes
    for r in range(num_sizes):
        turtle.forward(100)
        turtle.left(angles)


for i in range(3, 11):
    draw_shapes(i)
    turtle.pencolor(random.random(), random.random(), random.random())


screen = Screen()
screen.exitonclick()
