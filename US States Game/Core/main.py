import time
import turtle
import pandas
from data import extract_data, create_new_data
from draw import Draw

# Vars
IMAGE = "../Data/blank_map.gif"
MISSING = "../Data/missing"
score = 0

# Screen init
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.register_shape(IMAGE)
screen.setup(width=800, height=800)

# Data of place and location
data = extract_data()
states = (data['state']).tolist()


# Turtle init
turtle.shape(IMAGE)

# Draw obj
draw = Draw()

while score < 50:
    time.sleep(0.8)
    guess = screen.textinput(f"{score} / 50", "Write here").title()

    if guess == 'Exit':
        break

    if guess in states:
        # Extracting X, Y
        states.remove(guess)
        row = data[guess == data.state]
        x = row.at[row.index[0], 'x']
        y = row.at[row.index[0], 'y']

        # Drawing
        draw.write_state(guess, x, y)

        # Score++
        score += 1

create_new_data(states, data)
