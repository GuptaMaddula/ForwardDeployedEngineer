from turtle import Turtle, Screen
import time

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_positions=[(0,0), (-20,0), (-40,0)]
timmies=[]

for position in starting_positions:
    tim=Turtle("square")
    tim.color("white")
    tim.penup()
    tim.goto(position)
    timmies.append(tim)

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)




    for seg_num in range(len(timmies)-1, 0, -1):
        new_x=timmies[seg_num-1].xcor()
        new_y=timmies[seg_num-1].ycor()
        timmies[seg_num].goto(new_x, new_y)

    timmies[0].forward(20)


               



screen.exitonclick()