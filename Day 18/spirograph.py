import turtle as t
import random

t.colormode(255)

turtle = t.Turtle()
turtle.speed(0)  # fastest
turtle.ht()

for i in range(90):
    turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.circle(150)
    turtle.right(4)

screen = t.Screen()
screen.exitonclick()
