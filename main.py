import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('TURTLE CROSSING')
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    for car in car_manager.all_cars :
        if car.distance(player) < 20 :
            game_is_on = False
            scoreboard.game_over()
    if player.is_at_finish_line() :
        player.go_to_start()
        car_manager.level_up()
        scoreboard.inc_level()
    
    
screen.exitonclick()