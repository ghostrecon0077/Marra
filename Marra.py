import discord
from discord.ext import commands
from allie.memory import init_db
import asyncio
from allie.handler import handle_allie_response  # 🔄 You’ll create this function in allie/handler.py
from dotenv import load_dotenv
import os
load_dotenv()


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# 🔒 Replace with your Discord user ID
ALLOWED_USER_ID = 251010583770562560

# 🧠 Replace with the channel ID where Allie Protocol should respond
ALLIE_CHANNEL_ID = 1382780791129505964  # 🚨 Replace this with your actual channel ID

@bot.check
async def globally_block_dms_and_users(ctx):
    return ctx.author.id == ALLOWED_USER_ID

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # 👁️ Allie Protocol listens in a specific channel
    if message.channel.id == ALLIE_CHANNEL_ID:
        await handle_allie_response(message)  # 🔄 Async handler for OpenRouter/DeepSeek
        return  # 🔕 Skip regular command processing

    # 🧹 Delete !command messages (optional)
    if message.content.startswith('!'):
        try:
            await message.delete()
        except:
            pass

    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    try:
        await ctx.message.delete()
    except:
        pass

    if isinstance(error, (commands.CheckFailure, commands.CommandNotFound, commands.MissingRequiredArgument)):
        return
    print(f"[ERROR] {type(error).__name__}: {error}")

@bot.event
async def on_ready():
    init_db()  # ✅ Initialize SQLite database
    await bot.change_presence(activity=discord.Game(name="⚡ Allie protocol: initializing soon"))
    print(f"[OK] Logged in as {bot.user} (ID: {bot.user.id})")
    print("[READY] Marra is up and running!")


async def load_cogs():
    extensions = [
        "cogs.welcome",
        "cogs.moderation",
        "cogs.setup"
    ]
    for ext in extensions:
        try:
            await bot.load_extension(ext)
            print(f"[LOAD] Loaded extension: {ext}")
        except commands.errors.ExtensionAlreadyLoaded:
            print(f"[SKIP] Extension {ext} is already loaded.")
        except Exception as e:
            print(f"[ERROR] Failed to load {ext}: {e}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv("DISCORD_BOT_TOKEN"))  # 🔐 Replace with your actual bot token

asyncio.run(main())
