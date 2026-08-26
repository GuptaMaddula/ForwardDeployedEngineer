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
from turtle import Screen
import random

timmy=t.Turtle()
t.colormode(255)

colours=["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen", "Violet", "Yellow", "Blue", "Green", "Indigo", "Orange", "Red"]

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    random_color=(r,g,b)
    return random_color

def drawshapes():
    
    def draw_shape(num_sides):
        angle=360/num_sides
        for _ in range(num_sides):
            timmy.forward(100)
            timmy.right(angle)


    for shape_side_n in range(3,20):
        timmy.pensize(10)
        timmy.shape("turtle")
        timmy.color(random_color())
        draw_shape(shape_side_n)



def random_walk():
    directions=[0,30,60,25,135,245,315,100,90,180,270,327, 57, 12, 140, 125, 114, 71, 52, 346, 279, 44, 302, 216, 16, 15, 47, 111, 119, 258, 308, 13, 287, 101, 332, 359, 279, 214, 112, 229, 301, 142, 3, 81, 357, 216, 174, 142, 79, 110, 172, 52, 47, 194, 49, 183, 176, 309, 135, 22, 235, 274, 63, 193, 40, 282, 150, 321, 316, 185, 295, 98, 360, 35, 23, 338, 116, 148, 40, 119, 51, 194, 142, 232, 325, 186, 83, 189, 181, 107, 343, 136, 359, 349, 331, 36, 311, 325, 87, 273, 125, 83, 236, 194, 138, 327, 352, 285, 112, 350, 166]
    timmy.pensize(10)


    for _ in range(100):
        timmy.shape("turtle")
        timmy.color(random_color())
        timmy.forward(50)
        timmy.setheading(random.choice(directions))

timmy.speed("fastest")

def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+size_of_gap)


# drawshapes()
# random_walk()

spirograph(0.5)

screen=Screen()
screen.exitonclick()










