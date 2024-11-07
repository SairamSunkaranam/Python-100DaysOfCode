from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong game")

screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(r_paddle.move_paddle_up, "Up")
screen.onkey(r_paddle.move_paddle_down, "Down")
screen.onkey(l_paddle.move_paddle_up, "w")
screen.onkey(l_paddle.move_paddle_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.bounce_x()

    if ball.xcor() > 390:
        scoreboard.left_score()
        ball.reset_position()

    if ball.xcor() < -390:
        scoreboard.right_score()
        ball.reset_position()

screen.exitonclick()
