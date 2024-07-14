import pandas


DATA = "../Data/50_states.csv"
NEW_DATA = "../Data/states_to_learn.csv"


data = pandas.read_csv(DATA)


def extract_data():
    return data


def create_new_data(states, dt: pandas.DataFrame):
    new_data = {
        'state': [],
        'x': [],
        'y': []
    }

    for state in states:
        row = dt[dt.state == state]
        x = row.x.item()
        y = row.y.item()
        new_data['state'].append(state)
        new_data['x'].append(x)
        new_data['y'].append(y)

    new_data = pandas.DataFrame(new_data)
    new_data.to_csv(NEW_DATA)

