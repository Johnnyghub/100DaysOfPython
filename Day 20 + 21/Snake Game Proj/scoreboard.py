from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file='high_score.txt', mode='r') as file:
            self.highscore = int(file.read())
        self.newHighScore = False
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(-5, 270)
        self.write(f"Score = {self.score} Highscore = {self.highscore}", align="center", font=("Arial", 14, "normal"))

    def foodEaten(self):
        self.score += 1
        self.clear()

        if self.score > self.highscore:  # if high score beaten, constantly update the scoreboard
            self.highscore = self.score
            self.newHighScore = True

        self.write(f"Score = {self.score} Highscore = {self.highscore}", align="center", font=("Arial", 14, "normal"))

    def gameOver(self):
        self.home()
        self.write(f"Game Over", align="center", font=("Arial", 14, "normal"))

        if self.newHighScore:
            with open(file='high_score.txt', mode='w') as file:
                file.write(str(self.highscore))
