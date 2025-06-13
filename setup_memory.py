import sqlite3

conn = sqlite3.connect("memory.db")
c = conn.cursor()

# 🧠 Create memory table with correct columns
c.execute("""
CREATE TABLE IF NOT EXISTS memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    user_message TEXT,
    bot_response TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("memory.db is ready with updated memory table.")
