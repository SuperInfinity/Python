import math
from tkinter import *
import time


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Courier", 20, 'bold')
FONT2 = ("Courier", 40, 'bold')
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✔"
SEC = 60
reps = 0
ticks = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def stop_timer():
    global reps
    global ticks
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    heading.config(text="Timer")
    tick.config(text="")
    reps = 0
    ticks = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global ticks
    reps += 1
    work_secs = WORK_MIN * SEC
    work_break_secs = SHORT_BREAK_MIN * SEC
    long_break_secs = LONG_BREAK_MIN * SEC

    if reps % 8 == 0:
        count_down(long_break_secs)
        heading.config(text='Long Break', fg=RED)
        ticks = 0
        tick.config(text="")
    elif reps % 2 == 0:
        count_down(work_break_secs)
        heading.config(text='Break', fg=PINK)
        ticks += 1
        t = ''
        t += TICK * ticks
        tick.config(text=t)
    else:
        heading.config(text='Work', fg=GREEN)
        count_down(work_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    t = f'{count_min} : {count_sec}' if count_sec > 9 else f'{count_min} : 0{count_sec}'
    canvas.itemconfig(timer_text, text=t)

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Die Tomate Technik")
window.config(padx=100, pady=50)
window.config(bg=YELLOW)


# The canvas
canvas = Canvas(width=205, height=225, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato_img)
timer_text = canvas.create_text(101, 120, text="00:00", fill="white", font=FONT)
canvas.grid(row=1, column=1)


# The Timer
heading = Label(text="Timer", fg=GREEN, background=YELLOW, font=FONT2)
heading.grid(row=0, column=1)


# Start Button
start = Button(text="Start")
start.grid(row=2, column=0)
start.config(command=start_timer)


# Reset Button
reset = Button(text="Reset", command=stop_timer)
reset.grid(row=2, column=2)


# The tick
tick = Label(text="", fg=GREEN, background=YELLOW)
tick.grid(row=3, column=1)


window.mainloop()

