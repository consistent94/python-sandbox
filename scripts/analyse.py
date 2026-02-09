import sqlite3

def analyze():
    conn = sqlite3.connect("database/events.db")
    cursor = conn.cursor()


    query = """
    SELECT year, COUNT(*) as events_count
    FROM events
    GROUP BY year
    ORDER BY year;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    print("\nAnalysis Results:")
    for row in results:
        print(row)

    conn.close()
if __name__ == "__main__":
    analyze()
