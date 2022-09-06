from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.speed('fastest')
        self.shapesize(stretch_len=4)
        self.penup()
        self.goto(0, -225)

    def moveLeft(self):
        if self.xcor() > -260:
            self.backward(20)

    def moveRight(self):
        if self.xcor() < 260:
            self.forward(20)
