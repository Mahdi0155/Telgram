import sqlite3

# اتصال به دیتابیس
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# ساخت جدول کاربران (اگر وجود نداشت)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE NOT NULL,
    username TEXT,
    grade TEXT,
    field TEXT,
    province TEXT,
    city TEXT,
    coins INTEGER DEFAULT 0
)
''')

# ساخت جدول سوالات (اگر وجود نداشت)
cursor.execute('''
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    question TEXT NOT NULL,
    answer TEXT
)
''')

conn.commit()

# ثبت یا به‌روزرسانی کاربر
def add_or_update_user(user_id, username, grade, field, province, city):
    cursor.execute('''
        INSERT INTO users (user_id, username, grade, field, province, city)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
            username=excluded.username,
            grade=excluded.grade,
            field=excluded.field,
            province=excluded.province,
            city=excluded.city
    ''', (user_id, username, grade, field, province, city))
    conn.commit()

# دریافت اطلاعات کاربر
def get_user(user_id):
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    return cursor.fetchone()

# اضافه کردن سکه
def add_coins(user_id, amount):
    cursor.execute('UPDATE users SET coins = coins + ? WHERE user_id = ?', (amount, user_id))
    conn.commit()

# کم کردن سکه
def deduct_coins(user_id, amount):
    cursor.execute('UPDATE users SET coins = coins - ? WHERE user_id = ?', (amount, user_id))
    conn.commit()

# گرفتن تعداد سکه‌های کاربر
def get_coins(user_id):
    cursor.execute('SELECT coins FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    return result[0] if result else 0

# ثبت سوال جدید
def add_question(user_id, question):
    cursor.execute('INSERT INTO questions (user_id, question) VALUES (?, ?)', (user_id, question))
    conn.commit()

# گرفتن سوالات بی‌پاسخ
def get_unanswered_questions():
    cursor.execute('SELECT id, question FROM questions WHERE answer IS NULL')
    return cursor.fetchall()

# پاسخ دادن به سوال
def answer_question(question_id, answer_text):
    cursor.execute('UPDATE questions SET answer = ? WHERE id = ? AND answer IS NULL', (answer_text, question_id))
    conn.commit()
    return cursor.rowcount > 0
