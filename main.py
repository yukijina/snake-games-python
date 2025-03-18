from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game 🐍")
screen.tracer(0)

starting_positions = [(0,0), (-20,0), (-40,0)]
segments = []

for position in starting_positions:
  segment = Turtle("square")
  segment.color("white")
  segment.penup()
  segment.goto(position)
  segments.append(segment)


is_game_on = True

while is_game_on:
  screen.update()
  time.sleep(0.1)
  
  for segment_num in range(len(segments)-1, 0, -1) :
    #parameter (start, stop, step). 
    # Start from turles[2],[1]
    #moved to the same position of the last segment
    #ex [3] moves to the position of [2].All moves to the positon of [0]
    new_x = segments[segment_num -1].xcor()
    new_y = segments[segment_num -1].ycor()
    segments[segment_num].goto(new_x, new_y)
  
  #after all segments are in the same cell, move to the first turtle  
  segments[0].forward(20)
  segments[0].left(90)
  



screen.exitonclick()