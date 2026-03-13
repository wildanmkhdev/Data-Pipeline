from utils.extract import scrape_products
from utils.transform import transform_data
from utils.load import save_to_csv


def main():

    print("===== EXTRACT =====")
    raw_data = scrape_products()

    print("Jumlah raw data:", len(raw_data))

    print("===== TRANSFORM =====")
    clean_data = transform_data(raw_data)

    print("Jumlah data setelah transform:", len(clean_data))

    print("===== LOAD =====")
    save_to_csv(clean_data)

    print("Pipeline selesai")


if __name__ == "__main__":
    main()