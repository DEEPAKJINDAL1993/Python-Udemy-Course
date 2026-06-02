import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
score = 0

data = pd.read_csv("50_states.csv")
states = data.state.to_list()
# print(states)

screen.addshape(image)
turtle.shape(image)

guess_turtle = turtle.Turtle()
guess_turtle.penup()
guess_turtle.hideturtle()
guess_turtle.pencolor('black')

# def get_mouse_click_coordinates(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coordinates)
# turtle.mainloop()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title = f"States {len(guessed_states)}/50", prompt = "What's another state name?").title()
    print(answer_state)

    if answer_state == 'Exit':
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        answer_data = data[data.state == answer_state]
        guess_turtle.setposition(x = answer_data.x.values[0],y = answer_data.y.values[0])
        guess_turtle.write(answer_state, align = "center", move= False, font = ("Arial", 14,"normal"))


if len(guessed_states) == 50:
    guess_turtle.goto(0,0)
    guess_turtle.write("You won!", align = "center", font = ("Arial", 14,"bold"))




screen.exitonclick()