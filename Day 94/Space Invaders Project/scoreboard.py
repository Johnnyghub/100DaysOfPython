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
        self.goto(-190, 320)  # score in top left
        self.write(f"Score: {self.score}", align="center", font=("Courier", 15, "bold"))

    def gameOver(self):
        self.home()
        self.write(f"Game Over", align="center", font=("Verdana", 40, "normal"))

    def win(self):
        self.home()
        self.write(f"You Win!", align="center", font=("Verdana", 40, "normal"))

    def destroyed_ship(self):
        self.score += 100
        self.updateScoreboard()
