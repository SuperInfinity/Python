from read_data import get_data
from datetime import datetime
from writer import send_mail


YEAR = 'year'
MONTH = 'month'
DAY = 'day'
NAME = 'name'
EMAIL = 'email'


# 1. Update the birthdays.csv
try:
    data = get_data()
except Exception as e:
    print(f"Error: {e}")
    data = [{NAME: 'null', EMAIL: 'null', YEAR: 0, MONTH: 0, DAY: 0}]

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.now().date()

for item in data:

    today = datetime.now().date()

    if today.day == item[DAY] and today.month == item[MONTH]:
        print(f"Works for {item[NAME]}")
        send_mail(item[NAME], item[EMAIL])


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
