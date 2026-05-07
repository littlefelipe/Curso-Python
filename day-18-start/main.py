import turtle as t
import random
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colors = (r,g,b)
    return colors
timmy = t.Turtle()
timmy.shape("turtle")
# for i in range(3, 11):
#     timmy.color()
#     angle = 360 / i
#     move = 0
#     while move < i:
#         timmy.forward(100)
#         timmy.right(angle)
#         move += 1
headings = [0, 90, 180, 270]
timmy.speed("fastest")
timmy.width(2)

circles = 0
def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

# while True:
#     timmy.color(random_color())
#     timmy.setheading(random.choice(headings))
#     timmy.forward(25)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()