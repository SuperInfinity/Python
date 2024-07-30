from random import choice
import smtplib


FILES = [
    "/home/tanmay/Python/birthday Wisher/Data/letter_templates/letter_1.txt",
    "/home/tanmay/Python/birthday Wisher/Data/letter_templates/letter_2.txt",
    "/home/tanmay/Python/birthday Wisher/Data/letter_templates/letter_3.txt"
]
CREDS = [
    "tdummy027@gmail.com",
    "gnqdafcvwpscybqh"
]
PORT = 587


def send_mail(name: str, email):
    print("Correct the dates")

    with smtplib.SMTP("smtp.gmail.com", port=PORT) as conn:
        conn.starttls()
        conn.login()

