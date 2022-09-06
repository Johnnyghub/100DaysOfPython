import turtle
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

game_is_on = True

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.moveUp, "Up")
screen.onkeypress(r_paddle.moveDown, "Down")
screen.onkeypress(l_paddle.moveUp, "w")
screen.onkeypress(l_paddle.moveDown, "s")

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.hit()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.hit()

    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.player_1_scored()

    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.player_2_scored()

screen.exitonclick()
