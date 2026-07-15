import sqlite3

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE,
    code TEXT UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS blocked(
    telegram_id INTEGER UNIQUE
)
""")

conn.commit()


def get_user_code(user_id):
    cursor.execute(
        "SELECT code FROM users WHERE telegram_id=?",
        (user_id,)
    )
    return cursor.fetchone()


def add_user(user_id, code):
    cursor.execute(
        "INSERT OR IGNORE INTO users(telegram_id,code) VALUES(?,?)",
        (user_id, code)
    )
    conn.commit()


def get_user_by_code(code):
    cursor.execute(
        "SELECT telegram_id FROM users WHERE code=?",
        (code,)
    )
    return cursor.fetchone()


def block(user_id):
    cursor.execute(
        "INSERT OR IGNORE INTO blocked VALUES(?)",
        (user_id,)
    )
    conn.commit()


def is_blocked(user_id):
    cursor.execute(
        "SELECT * FROM blocked WHERE telegram_id=?",
        (user_id,)
    )
    return cursor.fetchone() is not None
