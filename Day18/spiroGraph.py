from turtle import Turtle, Screen
import random

def getRGB():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

def spirograph(n):
    screen = Screen()
    screen.colormode(255)

    turtle = Turtle()
    turtle.speed("fastest")
    turtle.width(4)
    angle = 360 / n

    for _ in range(n):
        turtle.color(getRGB())
        turtle.circle(100)
        turtle.left(angle)

    screen = Screen()
    screen.exitonclick()

spirograph(50)