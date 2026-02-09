import pandas as pd

def transform():
     df = pd.read_csv('data/raw_events.csv')

     df['date'] = pd.to_datetime(df['date'], errors='coerce')
     df = df.dropna(subset=["date", "event"])
     df['year'] = df['date'].dt.year
     df.to_csv('data/transformed_events.csv', index=False)

     if df.empty:
          raise ValueError("Dataset is empty")

     if "date" not in df.columns:
          raise ValueError("Missing date column")


     print('Transformed data saved to data/transformed_events.csv')
     print('row count after transformation:', len(df))

if __name__ == '__main__':
    transform()