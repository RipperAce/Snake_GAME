from tkinter import X
from turtle import Turtle

DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake():
    """A Class to Create snake of snake game
    
    Attributes: segments --> Array of turtles to create 3 size snake at beginning

                head --> stores head (turtle) of snake
    
    Methods: add_seg(pos) --> Add new segment to snake end
             
             create_snake() --> Creates snake of length 3
             
             extend_snake() --> extends snake by 1 length

             move() --> move snake by 20 distance forward
             
             up(), down(), left(), right() --> Turns heading of snake to up, down, left, right respectively"""

    def __init__(self):
        self.sgements = []
        self.create_snake()
        self.head = self.sgements[0]

    def add_seg(self, pos):
        new_segment = Turtle()
        new_segment.shape('square')
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(x=pos)
        self.sgements.append(new_segment)

    def create_snake(self):
        """create_snake(self) --> parameters: None,  return: None
        It creates snake of length 3"""
        for pos in range(3):
           self.add_seg((DISTANCE * (-pos), 0.0))
            

    def extend_snake(self):
        """extend_snake(self) --> parameters: None,  return: None
        It extends snake by 1 length"""
        self.add_seg(self.sgements[-1].position())

    def move(self):
        """move(self) --> parameters: None,  return: None
        It moves snake by 20 distance forward"""
        for segment_number in range(len(self.sgements)-1, 0, -1):
            xval, yval = self.sgements[segment_number-1].pos()
            self.sgements[segment_number].goto(xval, yval)
        self.head.forward(DISTANCE)

    def up(self):
        """up(self) --> parameters: None,  return: None
        It turns heading of snake to north"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """down(self) --> parameters: None,  return: None
        It turns heading of snake to south"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """left(self) --> parameters: None,  return: None
        It turns heading of snake to west"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """right(self) --> parameters: None,  return: None
        It turns heading of snake to east"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)