import discord
from discord.ext import commands
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="Your API Key",  # Replace with your key
)

ALLIE_CHANNEL_ID = Your CHANNEL ID  # Replace with your Allie-only channel ID

class AllieProtocol(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if (
            message.author.bot
            or message.channel.id != ALLIE_CHANNEL_ID
            or not message.content.strip()
        ):
            return

        async with message.channel.typing():
            response = client.chat.completions.create(
                model="deepseek/deepseek-r1-0528-qwen3-8b:free",
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
                        "content": message.content
                    }
                ]
            )
            await message.channel.send(response.choices[0].message.content)

async def setup(bot):
    await bot.add_cog(AllieProtocol(bot))
