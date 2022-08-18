import turtle
import time

t = turtle.Turtle()

screen = turtle.Screen()
screen.tracer(0)

def move():
    t.forward(10)

keysPressed = set()

actions = {
    "Up" : move
}

def click():
    for key in keysPressed:
        actions[key]()
    screen.update()
    condition = True

screen.onkeypress(lambda : keysPressed.add("Up"), "Up")
screen.onkeyrelease(lambda : keysPressed.remove("Up"), "Up")
screen.listen()

screen.ontimer(move, 1)

#click()

condition = True
screen.ontimer(click, 100)
condition = False

screen.exitonclick()