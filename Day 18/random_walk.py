import turtle as t
import random

t.colormode(255)

turtle = t.Turtle()

turtle.speed(10)
turtle.pensize(10)

directions = [0, 90, 180, 270]

for i in range(300):
    turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.seth(random.choice(list(directions)))
    turtle.forward(30)

screen = t.Screen()
screen.exitonclick()
