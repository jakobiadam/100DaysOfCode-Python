from food import Food
from scoreBoard import ScoreBoard
from snake import Snake

import turtle
import time

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