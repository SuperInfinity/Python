import datetime as dt


FILE = "../Data/quotes.txt"


def read_quotes():
    with open(FILE, 'r') as f:
        lines = f.readlines()

    return lines