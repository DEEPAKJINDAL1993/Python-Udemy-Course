from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

p1 = Paddle(color = 'white',position=(350,0))
p2 = Paddle(color = 'white',position=(-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.update()

screen.listen()
screen.onkeypress(p1.up,key='p')
screen.onkeypress(p1.down,key='l')
screen.onkeypress(p1.up,key='Up')
screen.onkeypress(p1.down,key='Down')

screen.onkeypress(p2.up,key='w')
screen.onkeypress(p2.down,key='s')
screen.onkeypress(p2.up,key='q')
screen.onkeypress(p2.down,key='a')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collisions with upper and lower walls, and bounce back
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(p1) < 50 and ball.xcor() > 330 or ball.distance(p2) < 50 and ball.xcor() <-330:
        ball.bounce_x()

    # Detect if right paddle misses the ball
    if ball.xcor() > 360:
        scoreboard.l_points()
        ball.reset()
        time.sleep(0.2)
        ball.move()

    # Detect if left paddle misses the ball
    if ball.xcor() < -360:
        scoreboard.r_points()
        ball.reset()
        time.sleep(0.2)
        ball.move()

    # Finish off the game if a player cross certain number of points
    if scoreboard.l_score == scoreboard.game_points or scoreboard.r_score == scoreboard.game_points:
        game_is_on = False
        scoreboard.game_over()











screen.exitonclick()
