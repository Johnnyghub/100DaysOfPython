from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.speed("fastest")
        self.seth(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def returnToStart(self):
        self.goto(STARTING_POSITION)

    def levelCompleted(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False
