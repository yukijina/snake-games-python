from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  """create snakes"""
  def __init__(self):
    self.snakes = []
    self.create_snake()  
    self.head = self.snakes[0]
    
  def create_snake(self):
    """create 3 snakes"""
    for position in STARTING_POSITION:
      self.add_snake(position)
     
  
  def add_snake(self, position):
    """create segments(snakes)"""
    snake = Turtle("square")
    snake.color("white")
    snake.penup()
    snake.goto(position)
    self.snakes.append(snake)
    
  def extend(self):
    """extend snake. add a snake at the last position"""
    self.add_snake(self.snakes[-1].position())
      
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
    self.head.forward(MOVE_DISTANCE)
  
  #snakes moves one direction only  
  def move_up(self):
    """Change snake's direction to up"""
    if self.head.heading() != DOWN:
      self.head.setheading(UP)
  
  def move_down(self):
    """Change snake's direction to down"""
    if self.head.heading() != UP:
      self.head.setheading(DOWN)
  
  def move_left(self):
    """Change snake's direction to left"""
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
    
  def move_right(self):
    """Change snake's directio to right"""
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
 
    
    