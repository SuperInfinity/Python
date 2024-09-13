from random import choice
import smtplib


FILES = [
    "/home/tanmay/Python/birthday Wisher/Data/letter_templates/letter_1.txt",
    "/home/tanmay/Python/birthday Wisher/Data/letter_templates/letter_2.txt",
    "/home/tanmay/Python/birthday Wisher/Data/letter_templates/letter_3.txt"
]
CREDS = [
    "tdummy027@gmail.com",
    "*************YOUR_PASSWORD*******"
]
PORT = 587


def send_mail(name: str, email):
    # Read The mail body
    file = choice(FILES)
    with open(file, 'r') as f:
        content = f.readlines()

    content[0] = content[0].replace('[NAME]', name)
    content = ''.join(content)

    print("Correct the dates")

    with smtplib.SMTP("smtp.gmail.com", port=PORT) as conn:
        conn.starttls()
        conn.login(user=CREDS[0], password=CREDS[1])
        conn.sendmail(
            from_addr=CREDS[0],
            to_addrs=email,
            msg=f"Subject:Happy Birthday {name}!\n\n{content}"
        )

