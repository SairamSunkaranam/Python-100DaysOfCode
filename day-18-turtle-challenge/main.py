import turtle, random
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)

    color_tuple = (r, b, g)
    return color_tuple


timmy.speed("fastest")
# for i in range(20):
# turtle.circle(50, 360)
# print(turtle.position())
# turtle.setposition(-100, 0)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100, 360)
        timmy.setheading(timmy.heading() + size_of_gap)
        # timmy.left(size_of_gap)


draw_spirograph(4)

screen.exitonclick()


# turtle.shape("circle")
# turtle.shapesize(5,2)
# turtle.tilt(45)
# timmy.width(1)
# timmy.right(360)

# timmy.width(10)
# timmy.speed(10)
#
# directions = [0, 90, 180, 270]
# screen = Screen()
# for _ in range(100):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))


# colors = ['red','green','blue','indianred','firebrick','ForestGreen']
#
# # def draw_shape(sides):
# #     for _ in range(sides):
# #         angle = 360 / sides
# #         timmy.forward(100)
# #         timmy.right(angle)
# #
# # for sides in range(3, 11):
# #     timmy.color(random.choice(colors))
# #     draw_shape(sides)



