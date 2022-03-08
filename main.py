from tkinter import NSEW
from turtle import Screen, colormode
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

"""_____ _   _          _  ________    _____          __  __ ______ 
  / ____| \ | |   /\   | |/ /  ____|  / ____|   /\   |  \/  |  ____|
 | (___ |  \| |  /  \  | ' /| |__    | |  __   /  \  | \  / | |__   
  \___ \| . ` | / /\ \ |  < |  __|   | | |_ | / /\ \ | |\/| |  __|  
  ____) | |\  |/ ____ \| . \| |____  | |__| |/ ____ \| |  | | |____ 
 |_____/|_| \_/_/    \_\_|\_\______|  \_____/_/    \_\_|  |_|______|"""

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

colormode(255)
segment_list = []
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
count = 0
sleep_time = 0.1

while game_on:
    screen.update()
    scoreboard.score_count(count)
    time.sleep(sleep_time)
    snake.move()

    if snake.head.distance(food.food) < 20:
        
        if len(snake.sgements) % 10 == 3:
            sleep_time -= 0.009

        snake.extend_snake()
        food.refresh()
        scoreboard.scoreboard.clear()
        count += 100

    if snake.head.xcor() > 299:
        snake.head.goto(-280, snake.head.ycor())
    elif snake.head.xcor() < -299:
        snake.head.goto(280, snake.head.ycor())
    elif snake.head.ycor() > 299:
        snake.head.goto(snake.head.xcor(), -280)
    elif snake.head.ycor() < -299:
        snake.head.goto(snake.head.xcor(), 280)

    for segment in snake.sgements[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_on = False
            break

screen.exitonclick()