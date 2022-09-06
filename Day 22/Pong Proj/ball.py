from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 1.3
        self.y_move = 1.3
        self.move_speed = 0.005

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1
        if self.move_speed > 0:
            self.move_speed -= 0.0005

    def reset_ball(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = 0.005
