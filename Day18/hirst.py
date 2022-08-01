import colorgram
from turtle import Turtle, Screen
import random

def find_colors(img):
    colors = colorgram.extract(img, 30)
    return [(color.rgb[0], color.rgb[1], color.rgb[2]) for color in colors]

def draw_row(turtle, colors, n):
    for _ in range(n):
        turtle.dot(20, random.choice(colors))
        turtle.forward(70)

def main():
    colors = find_colors('hirst.jpg')[3:]

    screen = Screen()
    screen.colormode(255)

    turtle = Turtle()
    turtle.pu()
    turtle.speed("fastest")
    turtle.hideturtle()
    starting_pos = [-315, -315]
    turtle.setposition(starting_pos[0], starting_pos[1])

    for _ in range(10):
        draw_row(turtle, colors, 10)
        starting_pos[1] += 70
        turtle.setposition(starting_pos[0], starting_pos[1])

    screen.exitonclick()

main()

