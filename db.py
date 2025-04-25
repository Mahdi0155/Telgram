import sqlite3

DB_NAME = "bot.db"

# ایجاد جدول‌ها (فقط یک بار اجرا میشه)
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            full_name TEXT,
            username TEXT UNIQUE,
            field TEXT,
            grade TEXT,
            province TEXT,
            city TEXT,
            coins INTEGER DEFAULT 5
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            question_text TEXT,
            answer_text TEXT
        )
    ''')
    conn.commit()
    conn.close()

# مدیریت کاربران
def add_or_update_user(user_id, full_name, username, field, grade, province, city):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO users (id, full_name, username, field, grade, province, city, coins)
        VALUES (?, ?, ?, ?, ?, ?, ?, 5)
    ''', (user_id, full_name, username, field, grade, province, city))
    conn.commit()
    conn.close()

def is_username_taken(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def get_user(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def remove_coins(user_id, amount):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET coins = coins - ? WHERE id = ?", (amount, user_id))
    conn.commit()
    conn.close()

# مدیریت سوالات
def add_question(user_id, question_text):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO questions (user_id, question_text)
        VALUES (?, ?)
    ''', (user_id, question_text))
    conn.commit()
    conn.close()

def get_unanswered_questions():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, question_text FROM questions WHERE answer_text IS NULL")
    questions = cursor.fetchall()
    conn.close()
    return questions

def answer_question(question_id, answer_text):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE questions SET answer_text = ? WHERE id = ?", (answer_text, question_id))
    conn.commit()
    success = cursor.rowcount > 0
    conn.close()
    return success
