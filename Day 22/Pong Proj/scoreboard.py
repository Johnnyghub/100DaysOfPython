from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(f"{self.player_1_score}", align="center", font=("Courier", 80, "bold"))
        self.goto(100, 180)
        self.write(f"{self.player_2_score}", align="center", font=("Courier", 80, "bold"))

    def gameOver(self):
        self.home()
        self.write(f"Game Over", align="center", font=("Verdana", 20, "normal"))

    def player_1_scored(self):
        self.player_1_score += 1
        self.updateScoreboard()

    def player_2_scored(self):
        self.player_2_score += 1
        self.updateScoreboard()
