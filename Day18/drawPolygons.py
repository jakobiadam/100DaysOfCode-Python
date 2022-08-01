from turtle import Turtle, Screen
import random

def draw_polygon(turtle, n):
    angle = 360 / n
    for _ in range(n):
        turtle.forward(100)
        turtle.right(angle)

def draw_polygons():
    screen = Screen()
    screen.colormode(255)

    timmy = Turtle()
    timmy.width(8)

    for i in range(3, 10):
        r = random.randint(1,255)
        g = random.randint(1,255)
        b = random.randint(1,255)
        timmy.pencolor((r, g, b))
        draw_polygon(timmy, i)

    screen.exitonclick()

draw_polygons()