from fcntl import FASYNC
from turtle import Turtle, Screen
import random
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [15, 45, 75, -15, -45, -75]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=- 230, y=y_pos[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("you won")
            else:
                print(f"you lost the winning color is {winning_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


# def move_forwards():
#     tim.forward(10)
# def move_backwards():
#     tim.back(10)
# def left():
#     tim.left(5)
# def right():
#     tim.right(5)
# def clear_screen():
#     tim.reset()
#
# screen.listen()
# screen.onkey(key = "w", fun = move_forwards)
# screen.onkey(key = "s", fun = move_backwards)
# screen.onkey(key = "a", fun = left)
# screen.onkey(key = "d", fun = right)
# screen.onkey(key = "c", fun = clear_screen)
screen.exitonclick()