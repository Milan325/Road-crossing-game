from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.move_inc = MOVE_INCREMENT
        self.move_dist = STARTING_MOVE_DISTANCE

    def create(self):
        rand_chance = randint(1, 6)
        if rand_chance == 2:
            car = Turtle("square")
            car.color("white")
            car.shapesize(stretch_len=2)
            car.penup()
            car.setheading(180)
            car.color(choice(COLORS))
            new_y = randint(-260, 260)
            car.goto(300, new_y)
            car.showturtle()
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move_dist)

    def speed_increase(self):
        self.move_dist += self.move_inc

