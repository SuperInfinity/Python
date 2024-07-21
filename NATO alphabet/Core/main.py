import pandas


DATA = "../Data/nato_phonetic_alphabet.csv"

data = pandas.read_csv(DATA)
new_data = {row.letter: row.code for i, row in data.iterrows()}

name = input("Enter a name: ").upper()
ans = []

for letter in name:
    if letter.isalpha():
        ans.append(new_data[letter])

print(f"The Nato Phonetic for {name.title()} is {ans}")
