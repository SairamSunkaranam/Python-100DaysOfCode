from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def move_anticlock():
    timmy.left(10)

def move_clock():
    timmy.right(10)

def clear_drawing():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_anticlock)
screen.onkey(key="d", fun=move_clock)
screen.onkey(key="c", fun=clear_drawing)


screen.exitonclick()
