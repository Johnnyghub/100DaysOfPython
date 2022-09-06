from turtle import *
import time
from player import Player
from scoreboard import Scoreboard
from enemy import Enemy
from laser import Laser
import random

screen = Screen()
screen.setup(width=500, height=700)
screen.tracer(0)
screen.title('Space Invaders')
screen.bgcolor('black')

screen.register_shape('./images/player.gif')
screen.register_shape('./images/enemy.gif')  # now we can use these shapes for the player and enemy classes

player = Player()
scoreboard = Scoreboard()

enemies = []
x_starts = [-160, -140, -160, -140]
y = 290

for i in range(4):
    x = x_starts[i]
    for j in range(8):  # 4 rows 8 columns of enemies
        enemies.append(Enemy((x, y)))
        x += 40
    y -= 55

lasers = []


def shoot(parent, friendly):
    if not friendly:
        lasers.append(Laser((parent.xcor(), parent.ycor()), False))  # no need for cooldown, will randomly select enemy to shoot every 2-5 seconds
        enemy_random_laser()  # recall firing the laser for the enemy
    else:
        if player.can_shoot:
            lasers.append(Laser((parent.xcor(), parent.ycor()), True))
            player.can_shoot = False
            screen.ontimer(t=500, fun=player.can_shoot_now)


def move_lasers():
    for laser in lasers:
        if -360 < laser.ycor() < 360:
            laser.move()
        else:
            lasers.remove(laser)
            laser.reset()
            laser.hideturtle()


def enemy_random_laser():
    try:
        screen.ontimer(t=random.randint(1500, 3000), fun=lambda: shoot(random.choice(enemies), False))  # randomly choose an enemy to fire a laser from
    except IndexError:
        pass  # when you win, this error will occur because enemies array is empty


screen.listen()
screen.onkey(player.moveLeft, 'a')
screen.onkeypress(player.moveLeft, 'a')
screen.onkey(player.moveLeft, 'Left')
screen.onkeypress(player.moveLeft, 'Left')
screen.onkey(player.moveRight, 'd')
screen.onkeypress(player.moveRight, 'd')
screen.onkey(player.moveRight, 'Right')
screen.onkeypress(player.moveRight, 'Right')
screen.onkeypress(lambda: shoot(player, True), 'space')

game_is_on = True
scoreboard.updateScoreboard()
left = True
enemy_random_laser()


def gameover():
    global game_is_on
    game_is_on = False  # use this so the last enemy/player gets a chance to disappear before the game ends
    screen.bye()  # close the screen, will also cause an error but we can ignore that I guess, the program is over and would've ended anyway


while game_is_on:
    time.sleep(0.01)
    screen.update()
    move_lasers()

    if len(enemies) != 0:  # so the game doesn't crash when the enemies are all dead
        if enemies[0].xcor() < -200:  # leftmost enemy
            left = True
        if enemies[-1].xcor() > 200:  # rightmost enemy
            left = False

        for enemy in enemies:
            if left:
                enemy.moveLeft()
            else:
                enemy.moveRight()

    for laser in lasers:
        if player.distance(laser) <= 40 and not laser.player_laser:
            laser.hideturtle()
            lasers.remove(laser)
            player.hideturtle()
            # TODO: Add explosion animation
            scoreboard.gameOver()
            screen.ontimer(t=3000, fun=gameover)  # let the enemies move and taunt you for 5 seconds before ending

        for enemy in enemies:
            if enemy.distance(laser) <= 40 and laser.player_laser:
                enemy.hideturtle()
                laser.hideturtle()
                enemies.remove(enemy)
                lasers.remove(laser)
                # TODO: Add explosion animation
                scoreboard.destroyed_ship()

    if len(enemies) == 0:  # all enemies destroyed
        scoreboard.win()
        screen.ontimer(t=3000, fun=gameover)

screen.mainloop()
