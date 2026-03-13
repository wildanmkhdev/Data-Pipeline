import pandas as pd


def transform_data(df):

    try:

        # hapus duplicate
        df = df.drop_duplicates()

        # hapus null
        df = df.dropna()

        # hapus produk invalid
        df = df[df["Title"] != "Unknown Product"]

        # hapus price unavailable
        df = df[df["Price"] != "Price Unavailable"]

        # hapus rating invalid
        df = df[~df["Rating"].str.contains("Invalid", na=False)]

        # convert price
        df["Price"] = df["Price"].str.replace("$", "", regex=False)
        df["Price"] = df["Price"].astype(float) * 16000

        # convert rating
        df["Rating"] = df["Rating"].str.replace("Rating: ⭐ ", "", regex=False)
        df["Rating"] = df["Rating"].str.replace(" / 5", "", regex=False)
        df["Rating"] = df["Rating"].astype(float)

        # convert colors
        df["Colors"] = df["Colors"].str.replace(" Colors", "", regex=False)
        df["Colors"] = df["Colors"].astype(int)

        # clean size
        df["Size"] = df["Size"].str.replace("Size: ", "", regex=False)

        # clean gender
        df["Gender"] = df["Gender"].str.replace("Gender: ", "", regex=False)

        return df

    except Exception as e:

        print("Error transform:", e)

        return pd.DataFrame()