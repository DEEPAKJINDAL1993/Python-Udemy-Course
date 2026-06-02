from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('turtle')
tim.color('red')

screen = Screen()
screen.colormode(255)

def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def draw_circle():
    tim.circle(30)

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkeypress(key='a', fun=turn_left)
screen.onkeypress(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear_screen)
screen.onkeypress(key='g', fun=draw_circle)

screen.exitonclick()
