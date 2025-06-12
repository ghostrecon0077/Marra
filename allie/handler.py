import os
import openai
import discord

# 🔐 Set your OpenRouter API key here or use an environment variable
OPENROUTER_API_KEY = "Your API Key"  # << Replace this

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

async def handle_allie_response(message: discord.Message):
    try:
        user_input = message.content.strip()

        response = client.chat.completions.create(
            model="deepseek/deepseek-r1-0528-qwen3-8b:free",
            extra_headers={
                "HTTP-Referer": "https://yourserver.com",  # Optional
                "X-Title": "Marra Protocol AI",             # Optional
            },
            messages=[
                {
                    "role": "system",
                    "content": (
    "You are Marra 2.0: Allie's Protocol, an advanced AI assistant. "
    "Reply clearly and directly. If asked 'Who are you?', respond 'I am Marra 2.0: Allie's Protocol.' "
    "If asked 'Who created you?', respond 'Marineo.' Stay professional, minimal emotion, and straight to the point."
)
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        reply = response.choices[0].message.content
        await message.channel.send(reply)

    except Exception as e:
        await message.channel.send("⚠️ The Allie Protocol encountered a shadow. (Error)")
        print(f"[Allie Error] {e}")
