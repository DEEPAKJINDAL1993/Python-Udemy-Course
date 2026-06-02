from turtle import Turtle, Screen
import random


screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)
user_bet = screen.textinput(title = 'Make a bet', prompt = 'Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

Turtles = {}
y_cordinate = -150
is_race_on = True

for color in colors:
    Turtles[color] = Turtle(shape='turtle')
    Turtles[color].color(color)
    Turtles[color].penup()
    Turtles[color].goto(x = -230, y = y_cordinate)
    y_cordinate += 50

if user_bet:
    is_race_on = True

winner = None

while is_race_on:
    for turtle in Turtles.values():
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() > 250:
            is_race_on = False
            winner = turtle
            print(winner.pencolor())
            if winner.pencolor() == user_bet:
                print(f'You\'ve won! your turtle  {winner.pencolor()} won the race.')
            else:
                print(f'You lost, {winner.pencolor()} won the race.')



screen.exitonclick()
