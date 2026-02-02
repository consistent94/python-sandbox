import pandas as pd

def extract():
    df = pd.read_csv('data/raw_events.csv')
    print(df.head())
    print('row count:', len(df))
    return df

if __name__ == '__main__':
    extract()