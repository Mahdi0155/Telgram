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

# اضافه کردن سکه به کاربر
def add_coins(user_id, amount):
    cursor.execute('UPDATE users SET coins = coins + ? WHERE user_id = ?', (amount, user_id))
    conn.commit()

# کم کردن سکه از کاربر
def remove_coins(user_id, amount):
    cursor.execute('UPDATE users SET coins = coins - ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
