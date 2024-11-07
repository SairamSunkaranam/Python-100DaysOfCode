from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.turtle_snake = []
        self.create_snake()
        self.head = self.turtle_snake[0]

    def create_snake(self):
        for position in self.positions:
            self.add_snake(position)

    def add_snake(self, position):
        new_timmy = Turtle("square")
        new_timmy.color("white")
        new_timmy.penup()
        new_timmy.setposition(position)
        self.turtle_snake.append(new_timmy)

    def move(self):

        for snake_number in range(len(self.turtle_snake) - 1, 0, -1):
            new_x = self.turtle_snake[snake_number - 1].xcor()
            new_y = self.turtle_snake[snake_number - 1].ycor()
            self.turtle_snake[snake_number].goto(new_x, new_y)

        self.head.forward(20)
        # return False

    def reset(self):
        for snake_n in self.turtle_snake:
            snake_n.goto(1000, 1000)
        self.turtle_snake.clear()
        self.create_snake()
        self.head = self.turtle_snake[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

