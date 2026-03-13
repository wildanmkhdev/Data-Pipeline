import sys
import os
import pandas as pd
from utils.extract import scrape_products
from unittest.mock import patch, Mock


# HTML dummy mirip struktur website
HTML_SAMPLE = """
<div class="collection-card">
    <div class="product-details">
        <h3 class="product-title">Test Shirt</h3>
        <div class="price-container">
            <span class="price">$10.00</span>
        </div>
        <p>Rating: ⭐ 4.5 / 5</p>
        <p>3 Colors</p>
        <p>Size: M</p>
        <p>Gender: Men</p>
    </div>
</div>
"""


@patch("utils.extract.requests.get")
def test_scrape_products(mock_get):

    # mock response object
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = HTML_SAMPLE

    mock_get.return_value = mock_response

    df = scrape_products()

    # cek dataframe dibuat
    assert isinstance(df, pd.DataFrame)

    # cek kolom ada
    assert "Title" in df.columns
    assert "Price" in df.columns
    assert "Rating" in df.columns

    # cek minimal ada data
    assert len(df) > 0