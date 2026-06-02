from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,color,position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(position)
        self.color(color)


    def up(self):
        if self.ycor() > 250:
            pass
        else:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() < -250:
            pass
        else:
            self.goto(self.xcor(), self.ycor() - 20)

