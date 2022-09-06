import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.075)

    snake.move()

    if snake.head.distance(food) < 15:
        food.foodEaten()
        scoreboard.foodEaten()
        snake.foodEaten()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.gameOver()

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameOver()

screen.exitonclick()
