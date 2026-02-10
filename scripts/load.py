import sqlite3 as sql
import pandas as pd

def load():
    df = pd.read_csv('data/cleaned_events.csv')
    conn = sql.connect('database/events.db')
    df.to_sql('events', conn, if_exists='replace', index=False)
    conn.close()
    print('Data loaded into data/events.db in table "events"')

if __name__ == '__main__':
    load()