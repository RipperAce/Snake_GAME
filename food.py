from turtle import Turtle
from random import randint

STRETCH_LEN = 0.5
STRETCH_WID = 0.5

class Food:
    """A Class to generate food for snake of snake game
    
    Attributes: food --> A turtle to display food
    
    Methods: refresh() --> Refreshes food on screen randomly after snake consumes food"""
    def __init__(self):
        new_item = Turtle()
        new_item.shape('circle')
        new_item.color('blue')
        new_item.shapesize(stretch_len=STRETCH_LEN, stretch_wid=STRETCH_WID)
        new_item.penup()
        self.food = new_item
        self.refresh()

    def refresh(self):
        """refresh(self) --> parameters: None,  return: None
        It generates food on screen randomly"""
        xval = randint(-280, 280)
        yval = randint(-280, 280)
        self.food.goto(xval, yval)