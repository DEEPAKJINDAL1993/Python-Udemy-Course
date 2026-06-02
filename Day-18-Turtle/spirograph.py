from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')
timmy.pensize(1)
timmy.speed(0)

screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


radius = 150
number_of_circles = 80

directions = (0,90,180,270)

for i in range(number_of_circles + 1):
    timmy.pencolor(random_color())
    angle = (360/number_of_circles)
    timmy.right(angle)
    timmy.circle(radius, 360, 12)
    i += 1

screen.exitonclick()




