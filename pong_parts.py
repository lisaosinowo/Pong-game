from turtle import Turtle

class Parts:

    def __init__(self):
        self.centre_dots()

    def centre_dots(self):
        for dots in range(-280, 300, 25):
            middle_dots = Turtle()
            middle_dots.shape("square")
            middle_dots.shapesize(stretch_wid=0.8, stretch_len=0.3, outline=1)
            middle_dots.color("white")
            middle_dots.speed("fastest")
            middle_dots.penup()
            middle_dots.setpos(0, dots)


        
