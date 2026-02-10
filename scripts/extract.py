import requests
import pandas as pd
import os

URL = "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&per_page=1000"
STATE_FILE = "data/state.txt"


def get_last_year():
    try:
        with open('data/last_year.txt', 'r') as f:
            content = f.read().strip()
            return int(content) if content else 2020
    except FileNotFoundError:
        return 2020


def save_last_year(year):
    with open(STATE_FILE, "w") as f:
        f.write(str(year))


def extract():
    print("Extracting incremental data...")

    last_year = get_last_year()

    response = requests.get(URL)
    data = response.json()[1]

    rows = []

    for item in data:
        if item["value"] is None:
            continue

        year = int(item["date"])

        if year > last_year:
            rows.append({
                "country": item["country"]["value"],
                "year": year,
                "population": item["value"]
            })

    df = pd.DataFrame(rows)

    if not df.empty:
        max_year = df["year"].max()
        save_last_year(max_year)

    df.to_csv("data/raw_events.csv", index=False)

    print("New rows extracted:", len(df))

    return df


if __name__ == "__main__":
    extract()
