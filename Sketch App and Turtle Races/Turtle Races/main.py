import random
from turtle import *

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle do you think will win? Enter the color: ")
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} Turtle is the winner")
            else:
                print(f"You Lost! The {winning_color} Turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()

