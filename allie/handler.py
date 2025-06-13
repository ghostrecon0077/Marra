import os
import discord
import openai
from allie.memory import save_interaction

import sqlite3
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# 🔐 Load OpenRouter API key securely
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# 🧠 SQLite DB connection
DB_PATH = "memory.db"
TABLE_NAME = "memory"

# 🤖 OpenRouter client
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

def save_to_memory(user_id, user_input, bot_response):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(f"""
        INSERT INTO {TABLE_NAME} (user_id, user_message, bot_response, timestamp)
        VALUES (?, ?, ?, ?)
    """, (user_id, user_input, bot_response, datetime.utcnow()))
    conn.commit()
    conn.close()

def fetch_memory(user_id, limit=5):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(f"""
        SELECT user_message, bot_response
        FROM {TABLE_NAME}
        WHERE user_id = ?
        ORDER BY timestamp DESC
        LIMIT ?
    """, (user_id, limit))
    results = c.fetchall()
    conn.close()
    return results[::-1]  # Oldest first

async def handle_allie_response(message: discord.Message):
    try:
        user_id = str(message.author.id)
        user_input = message.content.strip()

        # 🧠 Fetch memory for user
        history = fetch_memory(user_id)

        context = [
            {
                "role": "system",
                "content": (
                    "You are Marra 2.0: Allie's Protocol. You are an expert assistant built to answer technical and "
                    "programming questions clearly. If asked 'Who are you?' say 'I am Marra 2.0: Allie's Protocol.' "
                    "If asked 'Who created you?' say 'Marineo.' Otherwise, provide direct answers and explanations."
                )
            }
        ]

        # 👁️ Add recent context to prompt (filter short messages)
        for user_msg, bot_msg in history:
            if len(user_msg) > 5 and len(bot_msg) > 5:
                context.append({"role": "user", "content": user_msg})
                context.append({"role": "assistant", "content": bot_msg})

        # ➕ Current user input
        context.append({"role": "user", "content": user_input})

        # 🧠 Call model
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1-0528-qwen3-8b:free",
            messages=context,
            extra_headers={
                "HTTP-Referer": "https://yourserver.com",  # Optional
                "X-Title": "Marra Protocol AI",             # Optional
            }
        )

        bot_reply = response.choices[0].message.content.strip()
        await message.channel.send(bot_reply)

        # 💾 Save conversation to memory
        save_to_memory(user_id, user_input, bot_reply)

    except Exception as e:
        await message.channel.send("⚠️ The Allie Protocol encountered a shadow. (Error)")
        print(f"[Allie Error] {e}")
