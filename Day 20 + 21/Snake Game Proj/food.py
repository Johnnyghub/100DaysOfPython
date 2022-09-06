from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.goto(random.randint(-275, 275), random.randint(-275, 275))

    def foodEaten(self):
        self.goto(random.randint(-275, 275), random.randint(-275, 275))
