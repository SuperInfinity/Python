FILE = "Data/raw_data.txt"


with open(FILE, 'r') as f:
    data = f.readline().split()
    letters = [e for e in data if e.isalpha()]
    data = {e: " " for e in letters}

with open("Data/data.csv", 'a') as f:
    for (k, i) in data.items():
        f.write(f"{k},\n")

