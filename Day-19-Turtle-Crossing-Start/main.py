import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.up, key='Up')

game_is_on = True
while game_is_on:

    # Generate a new car every 6th time in the loop
    car_manager.refresh_cars()

    time.sleep(0.1)
    screen.update()

    # Detect collision with cars
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect collision with upper wall
    if player.is_at_finish_line():
        scoreboard.refresh()
        player.restart()
        car_manager.increase_speed()



screen.exitonclick()