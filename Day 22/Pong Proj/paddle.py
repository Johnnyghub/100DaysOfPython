from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_len=6)
        self.seth(90)
        self.penup()
        self.goto(x, 0)

    def moveUp(self):
        if self.ycor() < 225:
            self.forward(20)

    def moveDown(self):
        if self.ycor() > -225:
            self.backward(20)
