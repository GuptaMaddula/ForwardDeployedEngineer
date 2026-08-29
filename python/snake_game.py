from turtle import Turtle, Screen

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

x_positions=[0, -20, -40]


for position in range(0, 3):
    tim=Turtle(shape="square")
    tim.color("white")
    tim.goto(x=x_positions[position], y=0)



screen.exitonclick()