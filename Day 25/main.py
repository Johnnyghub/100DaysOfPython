import turtle
import pandas

correct_answers = []

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
screen.setup(width=725, height=491)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
answer_state = screen.textinput(title="Guess the State", prompt="Enter a state's name:").title()

game_is_on = True
first_loop = True
while game_is_on:

    if not first_loop:
        answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct", prompt="Enter another state's name:").title()

    first_loop = False

    if answer_state == '' or answer_state == 'Exit':
        game_is_on = False
        pandas.DataFrame([state for state in data.state if state not in correct_answers]).to_csv("states_to_learn.csv")
        # outputs missed states to csv file

    for state in data.state:
        if answer_state == state:
            if state not in correct_answers:
                correct_answers.append(state)
                t = turtle.Turtle()
                t.penup()
                t.hideturtle()
                t.speed("fastest")
                t.goto(int(data[data.state == state].x), int(data[data.state == state].y))
                t.write(state)

    if len(correct_answers) == 50:
        game_is_on = False

screen.exitonclick()
