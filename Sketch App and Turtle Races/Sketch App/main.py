from turtle import *

turtle = Turtle()
screen = Screen()


def go_foward():
    turtle.forward(10)


def go_left():
    turtle.left(10)


def go_back():
    turtle.backward(10)


def go_right():
    turtle.right(10)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(key="Right", fun=go_foward)
screen.onkey(key="Up", fun=go_left)
screen.onkey(key="Left", fun=go_back)
screen.onkey(key="Down", fun=go_right)
screen.onkey(key="space", fun=clear)
screen.exitonclick()

