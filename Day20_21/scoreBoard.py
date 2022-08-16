import turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class ScoreBoard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setpos(0, 270)
        self.pendown()
        self.score = 0

    def writeScore(self):
        self.write(f"Score : {self.score}", align = ALIGNMENT, font = FONT)

    def gameOver(self):
        self.penup()
        self.setpos(-60, 240)
        self.pendown()
        self.write(f"Game Over!\n  Score : {self.score}", font=('Arial', 20, 'normal'))

    def incrementScore(self):
        self.score += 1

    def clearScore(self):
        self.clear()