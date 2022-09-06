import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key='Up', fun=player.move)

game_is_on = True
loop = 7  # loop number to spawn cars
while game_is_on:
    time.sleep(0.02)
    screen.update()
    loop += 1

    if loop == 8:
        car_manager.spawnCar()
        loop = 1

    car_manager.move(scoreboard.level)

    for car in car_manager.Cars:
        if player.distance(car) < 20:
            scoreboard.gameOver()
            game_is_on = False

    if player.levelCompleted():
        scoreboard.nextLevel()
        player.returnToStart()

screen.exitonclick()
