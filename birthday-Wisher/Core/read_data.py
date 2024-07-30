from pandas import read_csv


FILE = "/home/tanmay/Python/birthday Wisher/Data/Birthdays/birthdays.csv"


def get_data():
    dataframe = read_csv(FILE)
    return dataframe.to_dict(orient="records")



