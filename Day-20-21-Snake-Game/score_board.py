from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 18, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.retrieve_high_score()
        self.pencolor('white')
        self.hideturtle()
        self.penup()
        self.refresh()

    def retrieve_high_score(self):
        with open('high_score.txt') as f:
            return int(f.read())


    def increase_score(self):
        self.score += 1
        self.refresh()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open('high_score.txt','w') as f:
            f.write(str(self.high_score))
        self.score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score : {self.score}    High Score : {self.high_score} ", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', move=False, align=ALIGNMENT, font=FONT)

