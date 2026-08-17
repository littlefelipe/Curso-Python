import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

states = data["state"].to_list()
guessed_states = []

def print_state(text, x, y):
    name = turtle.Turtle()
    name.hideturtle()
    name.penup()
    name.goto(x, y)
    name.write(text)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another states's name?").title()
    print(answer_state)
    if answer_state == 'Exit':
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        print("true")
        state_data = data[data.state == answer_state]
        print_state(answer_state,state_data.x.item(), state_data.y.item())


