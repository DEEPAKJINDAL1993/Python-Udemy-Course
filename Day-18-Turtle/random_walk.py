from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')
timmy.pensize(10)
timmy.speed('fastest')

screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


length = 30

directions = (0,90,180,270)


for i in range(100):
    timmy.pencolor(random_color())
    timmy.setheading(random.choice(directions))
    timmy.forward(length)
    i +=1


screen.exitonclick()




