import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_list = data["state"].to_list()
game_score = 0
game_total = len(data_list)
guessed_states_list = []
missed_states = []

game_on = True
while game_on:

    state_guess = screen.textinput(title=f"{game_score} / {game_total} guess the state", prompt="state name??").capitalize()

    if state_guess == "Exit":
        for state in data_list:
            if state not in guessed_states_list:
                missed_states.append(state)
                your_missed_states = pandas.DataFrame(missed_states)
                your_missed_states.to_csv("your_missed_states.csv")
        break

    if state_guess in data_list:
        data_state = data[data.state == state_guess]
        print(data_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(float(data_state.x), float(data_state.y))
        t.write(f"{state_guess}")
        game_score += 1
        guessed_states_list.append(state_guess)
    else:
        print("not a state")

    if game_score == game_total:
        game_on = False




