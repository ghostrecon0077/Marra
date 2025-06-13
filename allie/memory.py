import sqlite3
import os

DB_FILE = os.path.join(os.path.dirname(__file__), "allie_memory.db")

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS memory (
            user_id TEXT,
            message TEXT,
            reply TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_interaction(user_id, message, reply):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('INSERT INTO memory (user_id, message, reply) VALUES (?, ?, ?)', (user_id, message, reply))
    conn.commit()
    conn.close()
