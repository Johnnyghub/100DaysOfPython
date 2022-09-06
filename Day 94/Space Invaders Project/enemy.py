from turtle import Turtle
import time
import random

MOVE_DISTANCE = 15


class Enemy(Turtle):
    def __init__(self, start_position):
        super().__init__()
        self.penup()
        self.goto(start_position)
        self.shape("./images/enemy.gif")
        self.speed("fastest")
        self.turtlesize(0.2)
        self.can_shoot = True  # there needs to be a cooldown on shooting

    def destroy(self):
        self.reset()
        self.hideturtle()

    def moveLeft(self):
        self.forward(1)

    def moveRight(self):
        self.backward(1)
