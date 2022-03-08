from tkinter import font
from turtle import Turtle

class ScoreBoard:
    """A Class to maintain scoreboard of snake game
    
    Attributes: scoreboard --> A turtle to maintain score
    
    Methods: game_over() --> displays game over on the screen
             
             score_count(count) --> counts score of game and displays at top right of screen"""
    def __init__(self):
        new_item = Turtle()
        new_item.penup()
        new_item.color('white')
        new_item.ht()
        self.scoreboard = new_item
        
    def game_over(self):
        """game_over(self) --> parameters: None,  return: None
        It generates text GAME OVER on screen"""
        self.scoreboard.goto(0, 0)
        self.scoreboard.write(arg="GAME OVER", align='center', font=("Arial", 30, "bold"))

    def score_count(self,count):
        """score_count(self, count) --> parameters: count,  return: None
        It generates score by increasing count on screen"""
        self.scoreboard.goto(230, 280)
        self.scoreboard.write(arg=f"Score: {count}", align='center', font=("Arial", 10, "normal"))