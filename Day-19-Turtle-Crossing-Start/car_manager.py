from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.number_cars = 0
        self.speed = 0.1
        self.move_increment = MOVE_INCREMENT
        self.move_distance = STARTING_MOVE_DISTANCE
        self.refresh_cars()

    def add_car(self):
        if random.randint(0, 6) == 0:
            new_car = Turtle(shape="square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randrange(-250, 250,10))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.cars.append(new_car)
            self.number_cars += 1

    def move_cars(self):
        for car in self.cars:
            car.backward(self.move_distance)

    def remove_car(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.clear()
                car.hideturtle()
                self.cars.remove(car)
                del car

    def refresh_cars(self):
        self.add_car()
        self.move_cars()
        self.remove_car()

    def increase_speed(self):
        self.move_distance += self.move_increment




