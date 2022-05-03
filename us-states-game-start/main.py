import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
my_turtle = turtle.shape(image)
all_data = pandas.read_csv("50_states.csv")
all_states = all_data["state"].to_list()
x_cords = all_data["x"]
y_cords = all_data["y"]
count = 0
guessed_states = []


def find_state():
    for i in range(len(all_states)):
        if all_states[i] == answer:
            new_turtle = turtle.Turtle()
            new_turtle.hideturtle()
            new_turtle.penup()
            new_turtle.goto(x_cords[i], y_cords[i])
            new_turtle.write(answer)
            guessed_states.append(all_states[i])


should_continue = True

while should_continue:
    if count < len(all_states):
        answer = screen.textinput(title=f"({count}/50) Guess the state", prompt="What's your answer?").title()
        if answer == "Exit":
            missing_states = [state for state in all_states if state not in guessed_states]
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            should_continue = False
            print(missing_states)
        find_state()
        count += 1




