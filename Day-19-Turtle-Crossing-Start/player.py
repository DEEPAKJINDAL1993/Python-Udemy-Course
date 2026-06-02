from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.shape('turtle')
        self.restart()

    def up(self):
        self.forward(MOVE_DISTANCE)


    def restart(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
