import sqlite3

# اتصال به دیتابیس
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# ساخت جدول کاربران
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    grade TEXT,
    major TEXT,
    province TEXT,
    city TEXT,
    coins INTEGER DEFAULT 5
)
""")

# افزودن یا آپدیت کاربر
def add_or_update_user(user_id, username, grade, major, province, city):
    cursor.execute("""
    INSERT OR REPLACE INTO users (user_id, username, grade, major, province, city)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, username, grade, major, province, city))
    conn.commit()

# بررسی تکراری نبودن یوزرنیم
def is_username_taken(username):
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchone() is not None

# گرفتن اطلاعات کامل کاربر
def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    return cursor.fetchone()

# کم کردن سکه
def decrease_coin(user_id, amount=1):
    cursor.execute("UPDATE users SET coins = coins - ? WHERE user_id = ?", (amount, user_id))
    conn.commit()

# زیاد کردن سکه
def increase_coin(user_id, amount=1):
    cursor.execute("UPDATE users SET coins = coins + ? WHERE user_id = ?", (amount, user_id))
    conn.commit()

# گرفتن تعداد سکه
def get_user_coins(user_id):
    cursor.execute("SELECT coins FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    return result[0] if result else 0
