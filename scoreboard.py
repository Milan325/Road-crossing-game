from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 1
        self.update_sb()

    def update_sb(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def level_inc(self):
        self.score += 1
        self.update_sb()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
