import random
import turtle as t

# import colorgram
#
# colors = colorgram.extract('hirst.jpg', 20)
# rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
#
# print(rgb_colors)

colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77)]

t.colormode(255)

screen = t.Screen()

turtle = t.Turtle()
turtle.speed("fastest")
turtle.shape("circle")
turtle.penup()
turtle.goto(-250, -250)
turtle.seth(0)
turtle.penup()

for i in range(10):
    for j in range(10):
        turtle.dot(15, random.choice(colors))
        if j != 9:
            turtle.forward(50)

    if turtle.heading() == 0:
        turtle.seth(90)
        turtle.forward(50)
        turtle.seth(180)
    else:
        turtle.seth(90)
        turtle.forward(50)
        turtle.seth(0)

turtle.hideturtle()

screen.exitonclick()
