import turtle as t
import random

t.colormode(255)

turtle = t.Turtle()

for i in range(3, 11):
    turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for j in range(i):
        turtle.forward(100)
        turtle.right(360/i)

screen = t.Screen()
screen.exitonclick()

cv = t.getcanvas()
cv.postscript(file="file_name.ps", colormode='color')  # generate ps file to turn into png???

