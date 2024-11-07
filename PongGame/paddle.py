from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, cords):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(cords[0], cords[1])
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_paddle_up(self):
        self.goto(self.xcor(), (self.ycor() + 20))

    def move_paddle_down(self):
        self.goto(self.xcor(), (self.ycor() - 20))



