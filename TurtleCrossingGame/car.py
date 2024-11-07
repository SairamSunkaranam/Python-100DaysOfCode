import turtle
import random

turtle.colormode(255)

class Car(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.random_color()
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)

    def move_car(self):
        self.forward(random.randint(5, 10))

    def random_color(self):
        r = random.randint(0, 255)
        b = random.randint(0, 255)
        g = random.randint(0, 255)

        self.color((r, b, g))