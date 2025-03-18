from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake:
  """create snakes"""
  def __init__(self):
    self.snakes = []
    self.create_snake()  
    
  def create_snake(self):
    for position in STARTING_POSITION:
      snake = Turtle("square")
      snake.color("white")
      snake.penup()
      snake.goto(position)
      self.snakes.append(snake)
    print(self.snakes)
      
  def move(self):
    for snake_num in range(len(self.snakes)-1, 0, -1) :
      #parameter (start, stop, step). 
      # Start from snakes[2],[1]
      #moved to the same position of the last segment
      #ex [3] moves to the position of [2].All moves to the positon of [0]
      new_x = self.snakes[snake_num -1].xcor()
      new_y = self.snakes[snake_num -1].ycor()
      self.snakes[snake_num].goto(new_x, new_y)
  
    #after all snakes are in the same cell, move to the first turtle  
    self.snakes[0].forward(MOVE_DISTANCE)
    