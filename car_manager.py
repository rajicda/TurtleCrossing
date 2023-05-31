from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.setheading(270)
        self.goto(300, random.randrange(-260, 300))

    def move_car(self):
        self.forward(STARTING_MOVE_DISTANCE)
