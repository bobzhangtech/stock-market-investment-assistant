import sqlite3

db_name = "indices.db"
con = sqlite3.connect(db_name)
cur = con.cursor()

cur.execute(
    """CREATE TABLE IF NOT EXISTS Indices (index TEXT, date TEXT, price REAL)"""
)

con.commit()
