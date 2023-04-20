from turtle import Turtle, Screen
import random


screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=400)
screen.title(
    "Welcome to the Turtle Race")
user_bet = screen.textinput(
    title="Make A Bet!", prompt="Who will win the race. Enter the color of turtle: ").lower()
colors = ["red", "green", "orange", "yellow", "blue", "purple", "pink"]
ypositions = [-70, -40, -10, 20, 50, 80, 110]
all_turtles = []
is_race_on = False
for i in range(0, 7):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-230, y=ypositions[i])
    all_turtles.append(tim)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You Won! The {winning_turtle} turtle is the winner.")
            else:
                print(f"You Lose! The {winning_turtle} turtle is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()
