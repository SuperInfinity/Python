import time
from tkinter import *
from process_data import save_data_de, save_data_fr, save_rm_data_de
from random import choice

GERMAN = "Deutsch"
ENGLISH = "English"
FRENCH = "French"
BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT = "../data/images/card_front.png"
CARD_BACK = "../data/images/card_back.png"
RIGHT = "../data/images/right.png"
WRONG = "../data/images/wrong.png"
FONT1 = ("Aerial", 40, "italic")
FONT2 = ("Aerial", 70, "italic")
german_data = save_data_de()
french_data = save_data_fr()
X, Y, Z = 400.0, 150.0, 260.0

curr_face = 0
curr_card = {}
first = True


# ---Functions
def save_data():
    global german_data
    save_rm_data_de(german_data)
    

def next_card():
    global curr_card, loop, curr_face, first
    window.after_cancel(loop)
    curr_face = 0
    curr_card = choice(german_data)
    canvas.itemconfig(title, text=GERMAN, fill="black")
    canvas.itemconfig(word, text=curr_card[GERMAN], fill="black")
    canvas.itemconfig(card, image=card_faces[0])

    loop = window.after(3000, flip_card)

    if not first:
        german_data.remove(curr_card)
        first = False


def flip_card():
    global curr_card, curr_face, loop
    window.after_cancel(loop)
    curr_face = (curr_face + 1) % 2
    canvas.itemconfig(card, image=card_faces[curr_face])
    if curr_face == 0:
        canvas.itemconfig(title, text=GERMAN, fill="black")
        canvas.itemconfig(word, text=curr_card[GERMAN], fill="black")
        window.after_cancel(loop)
    else:
        canvas.itemconfig(title, text=ENGLISH, fill="white")
        canvas.itemconfig(word, text=curr_card[ENGLISH], fill="white")
        window.after(3000, flip_card)


# ---UI
window = Tk()
window.title("Flash-Card")
window.config(width=500, height=500, padx=50, pady=50, background=BACKGROUND_COLOR)

# --CANVAS
card_back_img = PhotoImage(file=CARD_BACK)
card_front_img = PhotoImage(file=CARD_FRONT)
card_faces = [card_front_img, card_back_img] # --- CARDS..!!!
canvas = Canvas(width=800, height=600, highlightthickness=0, background=BACKGROUND_COLOR)
card = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

#  --Text
# -Language
title = canvas.create_text(X, Y, text="", font=FONT1, tags="heading")

# -The Word
word = canvas.create_text(X, Z, text="", font=FONT2, tags="word")

# --BUTTONS
right_img = PhotoImage(file=RIGHT, width=100, height=100)
wrong_img = PhotoImage(file=WRONG, width=100, height=100)

# -right
right = Button(image=right_img, highlightthickness=0, background=BACKGROUND_COLOR, command=next_card)
right.grid(row=2, column=0)

# -wrong
wrong = Button(image=wrong_img, highlightthickness=0, background=BACKGROUND_COLOR, command=flip_card)
wrong.grid(row=2, column=1)


loop = window.after(3000, flip_card)
next_card()

window.mainloop()



