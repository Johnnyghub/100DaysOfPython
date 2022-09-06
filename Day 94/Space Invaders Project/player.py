from turtle import Turtle
import time

STARTING_POSITION = (0, -275)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("./images/player.gif")
        self.speed("fastest")
        self.turtlesize(0.2)
        self.can_shoot = True  # there needs to be a cooldown on shooting

    def moveLeft(self):
        if self.xcor() > -230:
            self.backward(MOVE_DISTANCE)

    def moveRight(self):
        if self.xcor() < 230:
            self.forward(MOVE_DISTANCE)

    def can_shoot_now(self):
        self.can_shoot = True
