import turtle

t = turtle.Turtle()
screen = turtle.Screen()

t.speed("fastest")


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def turn_clockwise():
    t.right(2)


def turn_counter_clockwise():
    t.left(2)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_clockwise, "d")
screen.onkeypress(turn_counter_clockwise, "a")  # failed to mention in lecture, make sure not to add () on functions
screen.onkey(clear, "c")
screen.listen()
screen.exitonclick()
