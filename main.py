import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
guessed = []
count = 0
data = pandas.read_csv("50_states.csv")
arr = data.state.to_list()
while len(guessed) < 50:

    answer_state = screen.textinput(title=f"{len(guessed)}/50 States", prompt="What's another state's name")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        # missing_states = []
        # for state in arr:
        #     if state not in guessed:
        #         missing_states.append(state)

        missing_states = [state for state in arr if state not in guessed]

        df = pandas.DataFrame(missing_states)
        df.to_csv("missed.csv")
        break

    if answer_state in arr:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.to_list()[0], state_data.y.to_list()[0])
        t.write(answer_state)
        guessed.append(answer_state)



