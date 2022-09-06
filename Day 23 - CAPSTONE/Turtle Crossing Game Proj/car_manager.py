from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 2.5


class CarManager:
    def __init__(self):
        self.Cars = []

    def spawnCar(self):
        car = Turtle()
        car.hideturtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(x=310, y=random.randint(-250, 250))
        car.seth(180)
        car.showturtle()
        self.Cars.append(car)

    def move(self, level):
        for car in self.Cars:
            car.forward(STARTING_MOVE_DISTANCE+((level-1)*MOVE_INCREMENT))
