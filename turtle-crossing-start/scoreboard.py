from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.clear()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-230, 250)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Level {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)

