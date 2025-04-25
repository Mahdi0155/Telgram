import sqlite3

# اتصال به دیتابیس (اگر نبود ایجاد میشه)
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

# ایجاد جدول کاربران
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
conn.commit()

# افزودن یا آپدیت کاربر
def add_or_update_user(user_id, full_name):
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    if user is None:
        cursor.execute('INSERT INTO users (user_id, full_name) VALUES (?, ?)', (user_id, full_name))
        conn.commit()

# به‌روزرسانی فیلد خاصی
def update_user_field(user_id, field, value):
    cursor.execute(f'UPDATE users SET {field} = ? WHERE user_id = ?', (value, user_id))
    conn.commit()

# گرفتن اطلاعات کاربر
def get_user(user_id):
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    return cursor.fetchone()

# چک کردن تکراری نبودن یوزرنیم
def is_username_taken(username):
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    return cursor.fetchone() is not None

# ایجاد جدول سوالات (اگر وجود نداشت)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        question TEXT,
        answer TEXT DEFAULT NULL,
        answered BOOLEAN DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()

# ذخیره سوال جدید
def save_question(user_id, question_text):
    cursor.execute('INSERT INTO questions (user_id, question) VALUES (?, ?)', (user_id, question_text))
    conn.commit()

# گرفتن سوالات پاسخ‌داده‌نشده
def get_unanswered_questions():
    cursor.execute('SELECT * FROM questions WHERE answered = 0')
    return cursor.fetchall()

# ثبت پاسخ به سوال
def answer_question(question_id, answer_text):
    cursor.execute('UPDATE questions SET answer = ?, answered = 1 WHERE id = ?', (answer_text, question_id))
    conn.commit()

# ایجاد جدول سوالات
cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        subject TEXT,
        question_text TEXT,
        answer_text TEXT DEFAULT NULL
    )
''')
conn.commit()

# افزودن سوال جدید
def add_question(user_id, subject, question_text):
    cursor.execute('INSERT INTO questions (user_id, subject, question_text) VALUES (?, ?, ?)',
                   (user_id, subject, question_text))
    conn.commit()

# گرفتن سوالات بدون پاسخ
def get_unanswered_questions():
    cursor.execute('SELECT * FROM questions WHERE answer_text IS NULL')
    return cursor.fetchall()

# پاسخ دادن به سوال
def answer_question(question_id, answer_text):
    cursor.execute('UPDATE questions SET answer_text = ? WHERE id = ?', (answer_text, question_id))
    conn.commit()

# گرفتن سوالات یک کاربر خاص
def get_user_questions(user_id):
    cursor.execute('SELECT * FROM questions WHERE user_id = ?', (user_id,))
    return cursor.fetchall()

# گرفتن سوالات یک کاربر خاص (مثلا برای نمایش تاریخچه)
def get_user_questions(user_id):
    cursor.execute('SELECT * FROM questions WHERE user_id = ?', (user_id,))
    return cursor.fetchall()

# اضافه کردن سکه به کاربر
def add_coins(user_id, amount):
    cursor.execute('UPDATE users SET coins = coins + ? WHERE user_id = ?', (amount, user_id))
    conn.commit()

# کم کردن سکه از کاربر
def remove_coins(user_id, amount):
    cursor.execute('UPDATE users SET coins = coins - ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
