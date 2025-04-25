# create_db.py
import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

# جدول کاربران
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE,
    full_name TEXT,
    grade TEXT,
    major TEXT,
    province TEXT,
    city TEXT,
    username TEXT UNIQUE,
    coins INTEGER DEFAULT 0
)
''')

# جدول سوالات
cursor.execute('''
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    question TEXT,
    answer TEXT DEFAULT NULL
)
''')

conn.commit()
conn.close()

print("Database created successfully.")
