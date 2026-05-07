from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.seth(90)
        self.penup()
        self.refresh()


    def move(self):
        self.goto(self.xcor(), self.ycor() + 10)

    def refresh(self):
        self.goto(STARTING_POSITION)