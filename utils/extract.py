
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time


def scrape_products():

    data = []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for page in range(1, 51):

        try:

            # Handle page pertama
            if page == 1:
                url = "https://fashion-studio.dicoding.dev/"
            else:
                url = f"https://fashion-studio.dicoding.dev/page{page}"

            print("Scraping:", url)

            response = requests.get(url, headers=headers)

            if response.status_code != 200:
                print("Gagal akses halaman:", page)
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            products = soup.find_all("div", class_="collection-card")

            print("Produk ditemukan:", len(products))

            for product in products:

                try:

                    # Title
                    title_tag = product.find("h3", class_="product-title")
                    title = title_tag.text.strip() if title_tag else None

                    # Price
                    price_tag = product.find("span", class_="price")
                    price = price_tag.text.strip() if price_tag else "Price Unavailable"

                    # Details (rating, colors, size, gender)
                    details = product.find_all("p")

                    rating = details[0].text.strip() if len(details) > 0 else None
                    colors = details[1].text.strip() if len(details) > 1 else None
                    size = details[2].text.strip() if len(details) > 2 else None
                    gender = details[3].text.strip() if len(details) > 3 else None

                    data.append({
                        "Title": title,
                        "Price": price,
                        "Rating": rating,
                        "Colors": colors,
                        "Size": size,
                        "Gender": gender,
                        "timestamp": datetime.now()
                    })

                except Exception as e:

                    print("Error parsing produk:", e)

        except Exception as e:

            print("Error page:", page, e)

        # Delay supaya tidak diblok server
        time.sleep(2)

    df = pd.DataFrame(data)

    print("Total data berhasil diambil:", len(df))

    return df