import sqlite3

conn = sqlite3.connect("restaurants.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS restaurants (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
lat REAL NOT NULL,
lng REAL NOT NULL,
offer TEXT
)
""")

cur.execute("DELETE FROM restaurants")

rows = [
    ("Sunrise Biscuit Co.", 33.76, -84.39, "Free hash browns over $8"),
    ("Peach Pit Burgers", 33.74, -84.36, "2-for-1 fries after 2PM"),
    ("Saigon Corner", 33.77, -84.41, "10% off banh mi"),
]

cur.executemany(
    "INSERT INTO restaurants (name, lat, lng, offer) VALUES (?, ?, ?, ?)",
    rows
)

conn.commit()
conn.close()
print("Seeded", len(rows), "restaurants")