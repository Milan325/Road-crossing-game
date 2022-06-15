from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """creates Scoreboard class using Turtle superclass"""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 1
        self.update_sb()

    def update_sb(self):
        """clears scoreboard and writes new score"""
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def level_inc(self):
        """increases score attribute and upadates scoreboard"""
        self.score += 1
        self.update_sb()

    def game_over(self):
        """writes "GAME OVER" at the center of the window"""
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
