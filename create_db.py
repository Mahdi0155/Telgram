# create_db.py

import sqlite3

# اتصال به دیتابیس (اگه وجود نداشته باشه، خودش میسازه)
conn = sqlite3.connect('data.db')  # یا هر اسمی که در پروژه استفاده کردی

cursor = conn.cursor()

# ساخت جدول users
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE,
    username TEXT,
    field TEXT,
    grade TEXT,
    province TEXT,
    city TEXT,
    coins INTEGER DEFAULT 0,
    free_coins INTEGER DEFAULT 0,
    invited_by INTEGER
)
''')

# ساخت جدول questions
cursor.execute('''
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    question_text TEXT,
    answer_text TEXT,
    status TEXT DEFAULT 'pending'
)
''')

conn.commit()
conn.close()

print("Database and tables created successfully!")
