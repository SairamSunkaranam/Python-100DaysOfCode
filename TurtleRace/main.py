from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
guess = screen.textinput("Place your Bet", "Enter the colour of the turtle that you bet on")
colours = ["red", "green", "blue", "yellow", "orange", "purple"]
race_is_on = False

turtles = []
x = -230
y = -80

for colour in colours:
    timmy = Turtle("turtle")
    turtles.append(timmy)
    timmy.penup()
    timmy.color(colour)
    timmy.setposition(x, y)
    y += 30


if guess:
    race_is_on = True

while race_is_on:
    for turtle in turtles:
        random_space = random.randint(0,10)
        turtle.forward(random_space)

        if turtle.xcor() > 230:
            race_is_on = False
            if turtle.pencolor() == guess:
                print(f"You've won the race. The winner turtle colour is {turtle.pencolor()}")
            else:
                print(f"You've lost the race. The winner turtle colour is {turtle.pencolor()}")


screen.exitonclick()