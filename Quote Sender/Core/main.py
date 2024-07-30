import random

from dt import read_quotes
import datetime as dt
import smtplib


email = "ur email"
password = "ur pasword"
dest = "dest email"
quotes = read_quotes()


now = dt.datetime.now()
print(now.weekday())
then = dt.datetime(day=1, year=2024, month=7)
print(then.weekday())

if now.weekday() == 1:
    quot = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=dest,
            msg=f"Subject:Monday's Motivation\n\n{quot}"
        )


