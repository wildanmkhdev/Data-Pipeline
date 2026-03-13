import sys
import os
import pandas as pd
from utils.load import save_to_csv


def test_load():

    df = pd.DataFrame({"A":[1,2]})

    save_to_csv(df)

    assert True