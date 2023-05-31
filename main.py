import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

player = Player()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

screen.onkey(key="Up", fun=player.move)
car_manager = CarManager()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with top line
    if player.ycor() > 280:
        player.player_reset()
        car_manager.increase_speed()
        scoreboard.next_level()

    # Detect collision player and car
    for car in car_manager.cars:
        if player.distance(car) < 30:
            player.player_reset()
            scoreboard.rest_level()
            game_is_on = False


screen.exitonclick()
