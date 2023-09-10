#Hirst Art Project
import turtle
import random
import colorgram as cg
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
turtle.colormode(255)

#list = []
#colors = cg.extract('image.jpg', 20)
#for num in range(20):
#    r = colors[num].rgb.r
#   g = colors[num].rgb.g
#  b = colors[num].rgb.b
# tup = (r, g, b)
#list.append(tup)
#print (list)

list_of_colors = [(246, 242, 235), (247, 240, 244), (239, 242, 247), (237, 245, 240), (212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183)]

y_count = -500
t.shape("turtle")
t.st()
t.color("green")
t.width(10)
t.speed("slow")
t.penup()

while y_count <= 400:
    x_count = -500
    while x_count <= 400:
        t.setpos(x_count, y_count)
        t.color(random.choice(list_of_colors))
        t.pendown()
        t.circle(5)
        t.penup()
        x_count += 100
    y_count += 100



screen.exitonclick()
