from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.speed("fastest")
        self.penup()
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level {self.level}", align="left", font=FONT)

    def gameOver(self):
        self.home()
        self.write(f"Game Over", align="center", font=FONT)

    def nextLevel(self):
        self.level += 1
        self.updateScoreboard()
