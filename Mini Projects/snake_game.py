from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
xpositions = [0, -20, -40]
segments = []
for turtle_indexes in range(0, 3):
    new_segments = Turtle(shape="square")
    new_segments.penup()
    new_segments.goto(x=xpositions[turtle_indexes], y=0)
    new_segments.color("white")
    segments.append(new_segments)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)
screen.exitonclick()
