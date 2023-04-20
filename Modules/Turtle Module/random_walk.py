import turtle as t
import random
tim = t.Turtle()
tim.shape("arrow")
tim.speed("fastest")
tim.hideturtle()
tim.pensize(15)
t.colormode(255)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]
for _ in range(200):
    tim.color(random_colors())
    tim.forward(30)
    tim.setheading(random.choice(directions))
tim = t.Screen()
tim.exitonclick()
