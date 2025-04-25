import sqlite3

def connect_db(): return sqlite3.connect("bot.db")

مدیریت کاربران

def add_or_update_user(user_id, full_name, username, grade, major, province, city): conn = connect_db() cursor = conn.cursor() cursor.execute(""" INSERT INTO users (id, full_name, username, grade, major, province, city, coins) VALUES (?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT(id) DO UPDATE SET full_name=excluded.full_name, username=excluded.username, grade=excluded.grade, major=excluded.major, province=excluded.province, city=excluded.city """, (user_id, full_name, username, grade, major, province, city, 0)) conn.commit() conn.close()

def is_username_taken(username): conn = connect_db() cursor = conn.cursor() cursor.execute("SELECT id FROM users WHERE username = ?", (username,)) result = cursor.fetchone() conn.close() return result is not None

مدیریت سوالات

def add_question(user_id, text): conn = connect_db() cursor = conn.cursor() cursor.execute("INSERT INTO questions (user_id, question) VALUES (?, ?)", (user_id, text)) conn.commit() conn.close()

def get_unanswered_questions(): conn = connect_db() cursor = conn.cursor() cursor.execute("SELECT id, question FROM questions WHERE answer IS NULL") questions = cursor.fetchall() conn.close() return questions

def answer_question(question_id, answer_text): conn = connect_db() cursor = conn.cursor() cursor.execute("UPDATE questions SET answer = ? WHERE id = ?", (answer_text, question_id)) conn.commit() success = cursor.rowcount > 0 conn.close() return success

