import turtle as t
import random
tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)


def random_colors():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return (r, b, g)


for i in range(40):
    tim.color(random_colors())
    tim.circle(100)
    tim.left(10)
tim = t.Screen()
tim.exitonclick()
