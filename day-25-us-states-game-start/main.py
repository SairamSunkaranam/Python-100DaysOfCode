from turtle import Turtle, Screen
import pandas

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
timmy = Turtle()
timmy.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:
    guess = screen.textinput(f"{len(guessed_states)}/50 States are correct", "Guess another state!").title()

    if guess == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pandas.DataFrame(missing_states).to_csv("out.csv")
        break
    if guess in all_states:
        new_timmy = Turtle()
        new_timmy.penup()
        new_timmy.hideturtle()
        guessed_states.append(guess)
        state_data = data[data.state == guess]
        new_timmy.goto(state_data.x.item(), state_data.y.item())
        new_timmy.write(f"{guess}")




