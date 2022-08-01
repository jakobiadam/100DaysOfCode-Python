from turtle import Turtle, Screen
import random

def getRGB():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

def randomWalk(rounds):
    screen = Screen()
    screen.colormode(255)
    turtle = Turtle()
    turtle.width(10)
    turtle.speed("fastest")

    turns = [0, 90, 180, 270]
    for _ in range(rounds):
        turtle.color(getRGB())
        if random.randint(0,1):
            turtle.left(random.choice([0,90]))
        else:
            turtle.right(random.choice([90,180]))

        turtle.forward(20)

    screen.exitonclick()

randomWalk(500)