import turtle

screen = turtle.Screen()
tim = turtle.Turtle()
turtle.speed("fastest")

def forward(obj = tim, unit = 10):
    obj.forward(unit)

def backward(obj = tim, unit = 10):
    obj.backward(unit)

def left(obj = tim, unit = 1):
    obj.setheading(obj.heading() + 10)

def right(obj = tim, unit = 1):
    obj.setheading(obj.heading() - 10)

def left_circle(obj = tim):
    obj.forward(1)
    obj.left(1)

def right_circle(obj = tim):
    obj.forward(1)
    obj.right(1)

def clear():
    screen.resetscreen()

def quit():
    screen.bye()

def sketch(screen = screen, tim = tim):

    screen.listen()

    screen.onkey(forward, 'w')
    screen.onkey(backward, 's')
    screen.onkey(left, 'a')
    screen.onkey(right, 'd')
    screen.onkey(left_circle, 'Up')
    screen.onkey(right_circle, 'Down')
    screen.onkey(clear, 'c')
    screen.onkey(quit, 'q')
    screen.onscreenclick(tim.goto)

    turtle.done()


if __name__ == "__main__":
    sketch()
