# from turtle import Turtle, Screen
# timmy=Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(200)
# timmy.right(90)
# timmy.forward(200)
# timmy.right(90)
# timmy.forward(200)
# timmy.right(90)
# timmy.forward(200)
# timmy.right(90)


# screen=Screen()
# screen.exitonclick()


import turtle as t
import random

timmy=t.Turtle()

colours=["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen", "Violet", "Yellow", "Blue", "Green", "Indigo", "Orange", "Red"]

def draw_shape(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for shape_side_n in range(3,20):
    timmy.shape("turtle")
    timmy.color(random.choice(colours))
    draw_shape(shape_side_n)


