from turtle import Turtle

#constants should be in caps
STARTING_POSITIONS=[(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    
    def __init__(self):
        self.timmies=[]
        self.create_snake()

    def create_snake(self):

        for position in STARTING_POSITIONS:
            tim=Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(position)
            self.timmies.append(tim)


    def move(self):
        for seg_num in range(len(self.timmies)-1, 0, -1):
            new_x=self.timmies[seg_num-1].xcor()
            new_y=self.timmies[seg_num-1].ycor()
            self.timmies[seg_num].goto(new_x, new_y)

        self.timmies[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.timmies[0].heading()!=DOWN:
            self.timmies[0].setheading(UP)

    def down(self):
        if self.timmies[0].heading()!=UP:
            self.timmies[0].setheading(DOWN)

    def left(self):
        if self.timmies[0].heading()!=RIGHT:
            self.timmies[0].setheading(LEFT)


    def right(self):
        if self.timmies[0].heading()!=LEFT:
            self.timmies[0].setheading(RIGHT)