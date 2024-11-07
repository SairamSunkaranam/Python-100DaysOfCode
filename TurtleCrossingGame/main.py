from turtle import Turtle, Screen
import time
from level import Level
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Race")
screen.tracer(0)

timmy = Turtle("turtle")
timmy.penup()
timmy.left(90)
timmy.goto(0, -280)


def move_up():
    timmy.forward(20)


def message_turtle(message, x_cor, y_cor):
    msg_turtle = Turtle()
    msg_turtle.clear()
    msg_turtle.penup()
    msg_turtle.hideturtle()
    msg_turtle.goto(x_cor, y_cor)
    msg_turtle.write(f"{message}", align="center")


level = Level()
screen.listen()
screen.onkey(move_up, "Up")
loop_run = 0
sleep_time = 0.1
game_level = 1
message_turtle(f"level {game_level}", -270, 280)

game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    # level.generate_random_cars(x_cor=(320, 324), y_cor=(-250, 250), no_of_cars=1)
    level.move_cars()

    for car in level.cars:
        if car.distance(timmy) < 15:
            message_turtle("game over", 0, 0)
            game_is_on = False

    if timmy.ycor() >= 280:
        timmy.goto(0, -280)
        game_level += 1
        message_turtle(f"level {game_level}", -270, 280)
        sleep_time *= 0.5

    if loop_run == 6:
        level.generate_random_cars((320, 321), (-250, 250), 1)
        loop_run = 0

    loop_run += 1


screen.exitonclick()