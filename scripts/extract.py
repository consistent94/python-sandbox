import requests
import pandas as pd

URL = 'https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&per_page=1000'

def extract():
    print('Extracting data from World Bank API...')
    response = requests.get(URL)
    data = response.json()

    records = data[1]

    rows = []

    for item in records:
        rows.append({
            "country": item["country"]["value"],
            "year": item["date"],
            "population": item["value"]
        })

    df = pd.DataFrame(rows)

    df.to_csv('data/raw_events.csv', index=False)

    print('Data extracted and saved to data/raw_events.csv', len(df), 'records extracted.')

    return df

if __name__ == '__main__':
    extract()