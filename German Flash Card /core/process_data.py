import csv
import pandas


FRENCH = "../data/raw/french_words.csv"
GERMAN = "../data/raw/german_words.csv"
REMAINDER = "../data/raw/rm_german_words.csv"


def save_data_fr():
    dataframe = pandas.read_csv(FRENCH)
    return dataframe.to_dict(orient="records")


def save_data_de():
    try:
        df = pandas.read_csv(REMAINDER)
    except FileNotFoundError:
        dataframe = pandas.read_csv(GERMAN)
        return dataframe.to_dict(orient="records")
    else:
        return df.to_dict(orient="records")


def save_rm_data_de(german_data: dict):
    dataframe = pandas.DataFrame(german_data, index=False)
    dataframe.to_csv(REMAINDER)

