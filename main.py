import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("TURTLE GAME")

a_player = Player()
car_men = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(a_player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_men.create()
    car_men.move_cars()


    for car in car_men.all_cars:
        if car.distance(a_player) < 20:
            game_is_on = False

    if a_player.ycor() > 280:
        car_men.speed_increase()
        a_player.finish()
        score_board.level_inc()

score_board.game_over()

screen.exitonclick()