import pandas


DATA = "../Data/nato_phonetic_alphabet.csv"

data = pandas.read_csv(DATA)
new_data = {row.letter: row.code for i, row in data.iterrows()}


def generate_phonetic():
    name = input("Enter a name: ").upper()
    try:
        ans = [new_data[e] for e in name]
    except KeyError:
        print("Only letters in the Alphabet please..!")
        generate_phonetic()
    else:
        print(f"The Nato Phonetic for {name.title()} is {ans}")
