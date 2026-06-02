from turtle import Turtle

FONT = ("Courier", 20, "normal")
GAME_POINTS = 5


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.game_points = GAME_POINTS
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.display_score()

    def l_points(self):
        self.l_score += 1
        self.display_score()

    def r_points(self):
        self.r_score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f'P2 Score: {self.l_score}', align='center', font=FONT)
        self.goto(200, 250)
        self.write(f'P1 Score: {self.r_score}', align='center', font=FONT)

    def game_over(self):
        if self.l_score == self.game_points:
            self.goto(0,100)
            self.write('P2 Wins!', align='center', font=FONT)
        elif self.r_score == self.game_points:
            self.goto(0,100)
            self.write('P1 Wins!', align='center', font=FONT)