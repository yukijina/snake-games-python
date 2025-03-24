from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game 🐍")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard  = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")


is_game_on = True

while is_game_on:
  screen.update()
  time.sleep(0.1)
  snake.move()
  
  #detect collision with turtle
  if snake.head.distance(food) < 15:
    print("hitting")
    food.refresh()
    scoreboard.add_score()
    snake.extend()
    
  #detect collision with wall
  if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
    scoreboard.reset()
    snake.reset()
    
  #detect collision with tail. Start from position 1 of the list
  for segment in snake.snakes[1:]:
    if segment == snake.head:
      pass
    elif snake.head.distance(segment) < 10:
      scoreboard.reset()
      snake.reset()

screen.exitonclick()