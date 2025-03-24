from turtle import Turtle
ALIGNMENT = "center"
FONT_STYLE = ("Courier New", 14, "bold")


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.high_score = 0
    self.color("white")
    self.penup()
    self.hideturtle()
    self.goto(0,280)
    self.display_score()

  
  def display_score(self):
    """display scoreboard"""
    self.clear()
    self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT_STYLE)
    
  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
    self.score = 0
    self.display_score()
      
  
  # def game_over(self):
  #   """display game over message with a final score"""
  #   self.goto(0,0)
  #   self.write(f"Game over🙈" , False, align=ALIGNMENT, font=FONT_STYLE)
    
  def add_score(self):
    """increase a score by 1 and clear current scoreboard"""
    self.score += 1
    self.clear()
    self.display_score()
    
    
  