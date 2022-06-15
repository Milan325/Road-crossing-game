from turtle import Turtle

# constants used as arguments for functions in Player class
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """the class creates Player object using Turtle superclass"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        """the module that moves Player object for 20px upwards"""
        self.forward(MOVE_DISTANCE)

    def finish(self):
        """the module checks if a Player object is at the top of the window"""
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)




