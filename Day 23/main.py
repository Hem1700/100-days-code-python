import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    # Detect player collision with car
    for car in car_manager.all_cars:
        if player.distance(car) <25:
            scoreboard.game_over()
            game_is_on = False
            screen.exitonclick()

	#safely reached to a finish line
    if player.finishline():
        player.go_to_start()
        car_manager.speed_up()
        scoreboard.score_up()