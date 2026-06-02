from turtle import Turtle
import random
import math


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.speed('fast')
        self.goto(0, 0)
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1
        self.move()

    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.9
        self.move()

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()