from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(-280, 250)
        self.write_score()

    def write_score(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.write_score()

    def rest_level(self):
        self.clear()
        self.write_score()
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)
