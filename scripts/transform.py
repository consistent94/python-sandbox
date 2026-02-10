import pandas as pd

def transform():
    df = pd.read_csv("data/raw_events.csv")

    df = df.dropna(subset=["population"])

    df["year"] = df["year"].astype(int)

    df.to_csv("data/cleaned_events.csv", index=False)

    print("Cleaned rows:", len(df))

if __name__ == "__main__":
    transform()