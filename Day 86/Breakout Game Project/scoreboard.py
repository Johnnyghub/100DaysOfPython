from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.goto(-250, -275)  # score in bottom left
        self.write(f"{self.score}", align="center", font=("Courier", 25, "bold"))

    def gameOver(self):
        self.home()
        self.write(f"Game Over", align="center", font=("Verdana", 40, "normal"))

    def broke_a_brick(self):
        self.score += 1
        self.updateScoreboard()
