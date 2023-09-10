#Turtle Race
import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starty = -150
all_turtles = []

for color in colors:
    t = Turtle("turtle")
    t.color(color)
    t.penup()
    t.goto(-230, starty)
    starty += 60
    all_turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won. The {winning_color} turtle has won!")
            else:
                print(f"You lost. The {winning_color} turtle has won!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()