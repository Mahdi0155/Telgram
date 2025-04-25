import sqlite3

# اتصال به دیتابیس یا ساخت فایل اگر وجود نداشته باشه
def connect_db():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    
    # ساخت جدول کاربران اگر وجود نداشت
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE,
            username TEXT UNIQUE,
            major TEXT,
            grade TEXT,
            province TEXT,
            city TEXT,
            coins INTEGER DEFAULT 0
        )
    ''')
    
    conn.commit()
    conn.close()

# اضافه کردن کاربر جدید
def add_user(telegram_id, username, major, grade, province, city, coins=5):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('''
        INSERT OR IGNORE INTO users (telegram_id, username, major, grade, province, city, coins)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (telegram_id, username, major, grade, province, city, coins))
    conn.commit()
    conn.close()

# گرفتن اطلاعات کاربر
def get_user(telegram_id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE telegram_id = ?', (telegram_id,))
    user = cur.fetchone()
    conn.close()
    return user

# آپدیت کردن تعداد سکه های کاربر
def update_coins(telegram_id, coins):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('UPDATE users SET coins = ? WHERE telegram_id = ?', (coins, telegram_id))
    conn.commit()
    conn.close()

# کم کردن یک سکه از کاربر
def decrease_coin(telegram_id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('UPDATE users SET coins = coins - 1 WHERE telegram_id = ?', (telegram_id,))
    conn.commit()
    conn.close()
