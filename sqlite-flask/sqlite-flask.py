import sqlite3

conn = sqlite3.connect("example.db")
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER
            )''')

cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 25))
conn.commit()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)
    
conn.close()