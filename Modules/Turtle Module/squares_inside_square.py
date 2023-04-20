from turtle import *
import random

tim = Turtle()

tim.color("Red")
tim.shape("arrow")
tim.hideturtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def change():
    tim.penup()
    tim.right(30)
    tim.forward(20)
    tim.left(30)


size = 200
move = 30
i = 1
while i <= 7:
    tim.color(random.choice(colours))
    for _ in range(4):
        tim.forward(size)
        tim.right(90)
    change()
    for _ in range(4):
        tim.pendown()
        tim.right(90)
    size = size - 30
    i = i + 1
tim = Screen()
tim.exitonclick()
