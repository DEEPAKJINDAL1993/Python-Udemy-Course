# import colorgram
#
# colors = colorgram.extract('damien.jpg',20)
# colors_rgb = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r,g,b)
#     colors_rgb.append(rgb)
#
# print(colors_rgb)

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')
timmy.pensize(1)
timmy.speed(0)

screen = Screen()
screen.colormode(255)


colors_rgb = [ (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188),
              (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49),
               (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111)]

timmy.teleport(-200, -200)

for j in range(10):
    for i in range(10):
        timmy.dot(20, random.choice(colors_rgb))
        timmy.teleport(timmy.xcor() + 50, timmy.ycor())
    timmy.teleport(-200, timmy.ycor() + 50)


screen.exitonclick()
