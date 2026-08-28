import pandas as pd

def clean_data(data):
    df = pd.DataFrame(data)

    df.drop_duplicates(subset=["title", "company"], inplace=True)
    df.fillna("N/A", inplace=True)

    return df