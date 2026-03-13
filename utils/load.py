import pandas as pd


def save_to_csv(df):

    try:
        df.to_csv("products.csv", index=False)
        print("Data berhasil disimpan ke products.csv")

    except Exception as e:
        print("Error load:", e)