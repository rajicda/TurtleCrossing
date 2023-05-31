import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            turtle = Turtle()
            turtle.shape("square")
            turtle.penup()
            turtle.color(random.choice(COLORS))
            turtle.shapesize(stretch_wid=1, stretch_len=2)
            turtle.setheading(180)
            turtle.goto(300, random.randrange(-250, 250))
            self.cars.append(turtle)

    def move_car(self):
        for car in self.cars:
            car.forward(self.car_speed)
            if car.xcor() < -300:
                car.hideturtle()

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

