#Drawings Circles with Turtle Display
import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()

turtle.colormode(255)
t.shape("circle")
t.ht()
t.color("green")
t.width(1)
t.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup

steps = random.randint(0, 100)

for num in range(steps):
    t.color(random_color())
    t.circle(100)

    if num < (num / 2):
        t.right(25)
        t.backward (25)
    else:
        t.left(25)
        t.forward(25)





screen.exitonclick()
