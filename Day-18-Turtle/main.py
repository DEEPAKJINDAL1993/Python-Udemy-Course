from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')

screen = Screen()
screen.colormode(255)


length = 100
angle = 0
max_sides = 10
#timmy.teleport(0,200)



for i in range(3,max_sides+1):
    tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    timmy.pencolor(tup)
    for j in range(0,i):
        timmy.forward(length)
        angle = 360/i
        timmy.right(angle)
        j += 1
    i +=1


for i in range(3,max_sides+1):
    tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    timmy.pencolor(tup)
    for j in range(0,i):
        timmy.forward(length)
        angle = 360/i
        timmy.left(angle)
        j += 1
    i +=1


for i in range(3,max_sides+1):
    tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    timmy.pencolor(tup)
    for j in range(0,i):
        timmy.backward(length)
        angle = 360/i
        timmy.right(angle)
        j += 1
    i +=1

for i in range(3,max_sides+1):
    tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    timmy.pencolor(tup)
    for j in range(0,i):
        timmy.backward(length)
        angle = 360/i
        timmy.left(angle)
        j += 1
    i +=1

screen.exitonclick()




