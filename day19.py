from turtle import  Turtle, Screen

t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def tilt_left():
    t.left(10)

def tilt_right():
    t.right(10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=tilt_left, key="a")
screen.onkey(fun=tilt_right, key="d")
screen.onkey(fun=clear, key="c")


screen.exitonclick()