import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.move_cars()

    car.generate_random_car()

    if player.reached_finish_line():
        car.level_up()
        score.level_up()
        player.referesh()

    for cars in car.cars:
        if cars.distance(player) < 20:
            score.game_over()
            game_is_on = False


screen.exitonclick()
