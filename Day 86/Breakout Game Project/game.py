from turtle import Screen, update
from paddle import Paddle
from ball import Ball
from bricks import Brick
from scoreboard import Scoreboard
import time

game_is_on = True

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

# create all the bricks
bricks = []
brick_x = -273
brick_y = 260
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']  #iterate so each row has a different color

for i in range(6):
    for j in range(12):
        bricks.append(Brick(colors[i], (brick_x, brick_y)))
        brick_x += 49
    brick_x = -273  # reset x position back to start of the line
    brick_y -= 25  # move y position down


screen.listen()
screen.onkey(paddle.moveLeft, 'Left')
screen.onkeypress(paddle.moveLeft, 'Left')
screen.onkey(paddle.moveRight, 'Right')
screen.onkeypress(paddle.moveRight, 'Right')


while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    for brick in bricks:
        if ball.distance(brick) < 30:
            ball.bounce_y()
            brick.hideturtle()
            bricks.remove(brick)  # remove the brick so we don't interact with it anymore
            scoreboard.broke_a_brick()

    # might miss if you hit in on the very edge, you need to trade off between visual appeal of closeless of hitting the paddle and being able to hit it from the edge
    if ball.distance(paddle) < 45 and ball.ycor() > -235:  # -225 is the paddle height, don't wanna hit the ball from the side of the paddle
        ball.bounce_y()

    if ball.ycor() < -315:
        game_is_on = False  # ball is off the map
        scoreboard.gameOver()

update()
screen.exitonclick()
