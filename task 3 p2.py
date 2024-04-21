import sqlite3

DATABASE = "urls.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS urls (
                    id INTEGER PRIMARY KEY,
                    long_url TEXT NOT NULL,
                    short_code TEXT NOT NULL UNIQUE);''')
    conn.commit()
    conn.close()

init_db()