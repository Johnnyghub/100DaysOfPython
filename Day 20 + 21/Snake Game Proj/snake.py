import turtle


def createNewSegment(position):
    t = turtle.Turtle()
    t.color("white")
    t.shape("square")
    t.penup()
    t.speed("fastest")
    t.goto(position)

    return t


class Snake:
    def __init__(self):
        self.snake = [createNewSegment(((i * -20), 0)) for i in
                      range(3)]  # snake's body consists of 3 squares at first
        self.head = self.snake[0]

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            self.snake[seg_num].goto(self.snake[seg_num - 1].xcor(), self.snake[seg_num - 1].ycor())  # basically snake follows itself

        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def foodEaten(self):
        self.snake.append(createNewSegment(self.snake[-1].position()))
