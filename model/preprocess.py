import pandas as pd

def load_data():
    data = pd.read_csv("data/dataset.csv")

    data.dropna(inplace=True)
    data["symptoms"] = data["symptoms"].str.lower()

    return data