from tkinter import *
from tkinter import messagebox
from pg import generate_password
import csv
import pyperclip


FILE = "Data/data.csv"


# ---------------------------- ACCESS THE MOST RECENT EMAIL ------------------------------- #
def read_recent_email():
    with open(FILE, 'r') as f:
        reader = csv.DictReader(f)
        for r in reader:
            em = r['email']
        username.insert(0, em)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def populate_password():
    ps = generate_password()
    pyperclip.copy(ps)
    password.insert(0, ps)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    wb = website.get()
    em = username.get()
    ps = password.get()
    data = {
        'website': wb,
        'email': em,
        'password': ps
    }

    if wb and em and ps:
        ans = messagebox.askokcancel(title=wb, message=f"These are the credentials entered\n email : {em}\n"
                                                       f"password : {ps}\n Do u want to save..?")

        if ans:
            with open(FILE, 'a') as f:
                writer = csv.DictWriter(f, fieldnames=data.keys())
                writer.writerow(data)

            clear_data()

    else:
        messagebox.showwarning(title="Error", message="Do Not Leave The Fields Empty..!")


def clear_data():
    website.delete(0, END)
    password.delete(0, END)
    username.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# The Window
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# The canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="Data/logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)


# --The Website row
# -The Label
label1 = Label(text="Website: ")
label1.grid(row=1, column=0)
# -The Entry
website = Entry(width=35)
website.grid(row=1, column=1, columnspan=2)
website.focus()

# --The Email Row
# -The Label
label2 = Label(text="Username/Email: ")
label2.grid(row=2, column=0)
# -The Entry
username = Entry(width=35)
username.grid(row=2, column=1, columnspan=2)

read_recent_email()

# --The Password
# -The Label
label3 = Label(text="Password: ")
label3.grid(row=3, column=0)
# -The Entry
password = Entry(width=35)
password.grid(row=3, column=1, columnspan=2)
# -Generate Button
g_password = Button(text="Generate Password", command=populate_password)
g_password.grid(row=3, column=2)

# --Add button
add = Button(text="Add", width=47, command=save_password)
add.grid(row=4, column=0, columnspan=3)


window.mainloop()

