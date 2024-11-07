import turtle
from turtle import Turtle, Screen
import random

colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
          (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
          (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
          (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60),
          (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]

timmy = Turtle()
screen = Screen()

turtle.colormode(255)
timmy.penup()
timmy.hideturtle()


def draw_dot_line(no_of_dots, dot_size, padding):
    for _ in range(no_of_dots):
        timmy.dot(dot_size, random.choice(colors))
        timmy.forward(padding)


for i in range(10):
    timmy.goto(-250, -200 + (i * 50))
    draw_dot_line(10, 20, 50)

screen.exitonclick()






# import colorgram
#
# colors = colorgram.extract('image.jpg', 100)
#
# extracted_colours = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     extracted_colours.append((r, g, b))
#
# print(extracted_colours)
