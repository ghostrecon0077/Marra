import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# ✅ Global check: Only allow one user (you)
@bot.check
async def globally_block_dms_and_users(ctx):
    allowed_user_id = 12345678901234567  # Replace with your Discord ID
    return ctx.author.id == allowed_user_id

# ✅ Delete every command message (even if successful)
@bot.event
async def on_message(message):
    if message.content.startswith('!') and not message.author.bot:
        try:
            await message.delete()
        except:
            pass
    await bot.process_commands(message)

# ✅ Silence all command errors from unauthorized users or missing commands
@bot.event
async def on_command_error(ctx, error):
    try:
        await ctx.message.delete()
    except:
        pass

    # Silently ignore permission issues or unknown commands
    if isinstance(error, (commands.CheckFailure, commands.CommandNotFound, commands.MissingRequiredArgument)):
        return

    # Optional: log real issues
    print(f"[ERROR] {type(error).__name__}: {error}")


@bot.event
async def on_ready():
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
        await bot.start("Your TOKEN")  # 🔐 Replace with your actual token

asyncio.run(main())
