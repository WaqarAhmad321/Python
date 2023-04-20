from turtle import Turtle, Screen

tim = Turtle()

tim.color("Red")
tim.shape("arrow")
for i in range(5):
    tim.left(72)
    tim.forward(100)
tim = Screen()
tim.exitonclick()
