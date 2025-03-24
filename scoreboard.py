from turtle import Turtle
ALIGNMENT = "center"
FONT_STYLE = ("Courier New", 14, "bold")


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.penup()
    self.hideturtle()
    self.goto(0,280)
    #self.high_score = 0
    with open("data.txt", "r") as file:
      self.high_score = int(file.read())
    self.update_scoreboard()

  
  def update_scoreboard(self):
    """update scoreboard"""
    self.clear()
    self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT_STYLE)
    
  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      self.update_datafile()
    self.score = 0
    self.update_scoreboard()
    
  def update_datafile(self):
    with open("data.txt", "w") as file:
      file.write(str(self.high_score))
      
  
  # def game_over(self):
  #   """update game over message with a final score"""
  #   self.goto(0,0)
  #   self.write(f"Game over🙈" , False, align=ALIGNMENT, font=FONT_STYLE)
    
  def add_score(self):
    """increase a score by 1 and clear current scoreboard"""
    self.score += 1  
    self.clear()
    self.update_scoreboard()
    

    
    
  