import pandas as pd

df = pd.read_csv('data/raw_events.csv')
print(df.head())
print('row count:', len(df))