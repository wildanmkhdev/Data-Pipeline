import pandas as pd
from utils.transform import transform_data


def test_transform_data_cleaning():

    # Data dummy seperti hasil scraping
    data = {
        "Title": ["T-shirt 1", "Unknown Product", "Jacket 3"],
        "Price": ["$10.00", "$20.00", "Price Unavailable"],
        "Rating": [
            "Rating: ⭐ 4.5 / 5",
            "Rating: ⭐ Invalid Rating / 5",
            "Rating: ⭐ 3.0 / 5"
        ],
        "Colors": ["3 Colors", "5 Colors", "2 Colors"],
        "Size": ["Size: M", "Size: L", "Size: XL"],
        "Gender": ["Gender: Men", "Gender: Women", "Gender: Unisex"]
    }

    df = pd.DataFrame(data)

    # jalankan fungsi transform
    result = transform_data(df)

    # hanya 1 data valid harus tersisa
    assert len(result) == 1

    # cek price sudah dikonversi ke rupiah
    assert result.iloc[0]["Price"] == 160000

    # cek rating float
    assert isinstance(result.iloc[0]["Rating"], float)

    # cek colors integer
    assert isinstance(result.iloc[0]["Colors"], int)

    # cek size sudah bersih
    assert result.iloc[0]["Size"] == "M"

    # cek gender sudah bersih
    assert result.iloc[0]["Gender"] == "Men"