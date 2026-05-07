import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

game_is_on = True

states = data["state"].to_list()
print(states)

def print_state(text, position):
    name = turtle.Turtle()
    name.hideturtle()
    name.penup()
    name.goto(position)
    name.write(text)

while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another states's name?")
    print(answer_state)
    if answer_state in states:
        print("true")
        print(data[data.state == answer_state].at["x"])
        print(data[data.state == answer_state].at["y"])
        #print_state(answer_state, (x, y))



screen.exitonclick()