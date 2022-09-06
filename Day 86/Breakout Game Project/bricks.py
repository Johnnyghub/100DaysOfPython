from turtle import Turtle


class Brick(Turtle):
    def __init__(self, color, position):
        super().__init__()
        self.color(color)
        self.shape('square')
        self.speed('fastest')
        self.shapesize(stretch_len=2.2, stretch_wid=0.8)
        self.penup()
        self.goto(position)


