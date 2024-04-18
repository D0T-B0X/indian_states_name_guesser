import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian states game")
image = "india-map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("state-names.csv")
data.set_index("state", inplace=True)
states = data.index.to_list()

states_guessed = []
while len(states_guessed) < 31:

    answer = turtle.textinput(title=f"{len(states_guessed)}/31  Guess the states", prompt="type your answer")

    if answer.title() in states:
        name = turtle.Turtle()
        name.hideturtle()
        name.penup()
        name.goto(x=data.loc[answer.title(), "x"], y=data.loc[answer.title(), "y"])
        name.write(f"{answer.title()}", font=("Courier", 12, "normal"))
        states_guessed.append(answer.title())
        states.remove(answer.title())

    if answer.title() == "Exit":
        new_data = pandas.DataFrame({'state': states})
        new_data.to_csv("states_to_learn.csv", index=False)
        break

turtle.exitonclick()
