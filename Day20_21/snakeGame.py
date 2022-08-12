import turtle
import numpy as np
import time
import random

class ScoreBoard:

    def __init__(self):
        self.cursor = turtle.Turtle()
        self.cursor.penup()
        self.cursor.color("white")
        self.cursor.hideturtle()
        self.cursor.setpos(-50, 270)
        self.cursor.pendown()
        self.score = 0

    def writeScore(self):
        self.cursor.write(f"Score : {self.score}", font = ('Arial', 20, 'normal'))

    def gameOver(self):
        self.cursor.penup()
        self.cursor.setpos(-60, 240)
        self.cursor.pendown()
        self.cursor.write(f"Game Over!\n  Score : {self.score}", font=('Arial', 20, 'normal'))

    def incrementScore(self):
        self.score += 1

    def clearScore(self):
        self.cursor.clear()

class Snake:
    startingPositions = [(0, 0), (-20, 0), (-40, 0)]

    def __init__(self):
        self.turnState = "right"
        self.snake = [turtle.Turtle(shape="square") for _ in range(3)]
        for i in range(3):
            (self.snake)[i].penup()
            (self.snake)[i].color("white")
            (self.snake)[i].setpos(self.startingPositions[i][0], self.startingPositions[i][1])

    def w(self):
        if self.turnState != "down":
            self.turnState = "up"

    def s(self):
        if self.turnState != "up":
            self.turnState = "down"

    def a(self):
        if self.turnState != "right":
            self.turnState = "left"

    def d(self):
        if self.turnState != "left":
            self.turnState = "right"

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].setpos(self.snake[i - 1].pos())
        self.moveHead()

    def moveHead(self):

        if self.turnState == "left" and self.snake[0].pos()[0] <= -300:
            self.snake[0].setpos(300, self.snake[0].pos()[1])

        elif self.turnState == "left":
            self.snake[0].setpos(self.snake[0].pos()[0] - 20, self.snake[0].pos()[1])

        elif self.turnState == "right" and self.snake[0].pos()[0] >= 300:
            self.snake[0].setpos(-300, self.snake[0].pos()[1])

        elif self.turnState == "right":
            self.snake[0].setpos(self.snake[0].pos()[0] + 20, self.snake[0].pos()[1])

        elif self.turnState == "up" and self.snake[0].pos()[1] >= 300:
            self.snake[0].setpos(self.snake[0].pos()[0], -300)

        elif self.turnState == "up":
            self.snake[0].setpos(self.snake[0].pos()[0], self.snake[0].pos()[1] + 20)

        elif self.turnState == "down" and self.snake[0].pos()[1] <= -300:
            self.snake[0].setpos(self.snake[0].pos()[0], 300)

        elif self.turnState == "down":
            self.snake[0].setpos(self.snake[0].pos()[0], self.snake[0].pos()[1] - 20)

    def addTail(self):
        newTail = turtle.Turtle(shape="square")
        newTail.penup()
        newTail.color("white")
        newTail.setpos(self.snake[-1].pos())
        self.move()
        self.snake.append(newTail)

    def testCollision(self):
        for i in range(1, len(self.snake)):
            if self.snake[i].pos() == self.snake[0].pos():
                return True
        else:
            return False

    def foodCollision(self, food):
        if (self.snake[0]).pos() == food.food.pos():
            return True
        else:
            return False

class Food:

    xPos = np.linspace(-300, 300, 31)
    yPos = np.linspace(-300, 300, 31)

    def __init__(self):
        self.food = turtle.Turtle(shape = "circle")
        self.food.penup()
        self.food.color("white")
        self.changePosition()

    def changePosition(self):
        (self.food).setpos(random.choice(self.xPos), random.choice(self.yPos))


def main():
    screen = turtle.Screen()
    screen.setup(width=620, height=620)
    screen.bgcolor("black")
    screen.tracer(False)
    screen.title("Snake")

    snake = Snake()
    food = Food()
    scoreBoard = ScoreBoard()
    scoreBoard.writeScore()
    screen.update()
    time.sleep(1)

    screen.onkey(snake.w, "Up")
    screen.onkey(snake.a, "Left")
    screen.onkey(snake.s, "Down")
    screen.onkey(snake.d, "Right")
    screen.listen()

    onGame = True
    isFoodCollision = False
    while onGame:
        if isFoodCollision:
            snake.addTail()
            isFoodCollision = False
        else:
            snake.move()

        if snake.testCollision():
            scoreBoard.clearScore()
            scoreBoard.gameOver()
            onGame = False

        elif snake.foodCollision(food):
            isFoodCollision = True
            food.changePosition()
            scoreBoard.incrementScore()
            scoreBoard.clearScore()
            scoreBoard.writeScore()

        screen.update()
        time.sleep(0.8 / len(snake.snake))

    screen.exitonclick()

if __name__ == "__main__":
    main()