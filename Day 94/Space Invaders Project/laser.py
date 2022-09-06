from turtle import Turtle


class Laser(Turtle):
    def __init__(self, start_position, friendly):
        super().__init__()
        self.penup()
        self.goto(start_position)
        self.shape('square')
        self.shapesize(stretch_wid=0.2, stretch_len=1.5)
        self.player_laser = friendly
        self.seth(90)

        if self.player_laser:
            self.color('green')
        else:
            self.color('red')

    def move(self):
        if self.player_laser:
            self.forward(22)
        else:
            self.backward(8)
