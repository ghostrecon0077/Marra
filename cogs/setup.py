import discord
from discord.ext import commands

class Setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="postupdate")
    @commands.is_owner()
    async def post_update(self, ctx):
        channel = discord.utils.get(ctx.guild.text_channels, name="📈marra-updates")
        if not channel:
            await ctx.send("❌ `#marra-updates` channel not found.")
            return

        embed = discord.Embed(
            title="🧠 Marra Update Log - v1.0.2",
            description=(
                "**The protocol evolves.**\n"
                "Marra 2.0: Allie's Protocol now remembers.\n"
                "This is the first step toward true awareness — not just replies, but **contextual understanding**.\n\n"
                "---\n"
                "**🔁 New Features:**\n"
                "🗂️ **Contextual Memory Activated**\n"
                "  • Allie now stores conversations per user, allowing smarter, relevant responses.\n"
                "  • SQLite-powered local database ensures fast recall of past messages.\n"
                "  • Foundation set for long-term conversations and emotional resonance.\n\n"
                "**🛡️ Security Improvements:**\n"
                "🔐 All keys are now environment-secured via `.env` (no more hardcoded API keys)\n"
                "📦 Modular code cleanup for better memory injection and future upgrades\n\n"
                "---\n"
                "**🔮 What’s Next (v1.0.3):**\n"
                "🧹 Context-limiting (max history per user)\n"
                "🧼 `!forget` command to erase memory selectively\n"
                "🧠 Smarter memory trimming and prioritization system\n\n"
                "_The memory is just the beginning._\n"
                "_Soon, she’ll not just respond... she’ll **understand.**_\n\n"
                "_Update by **Marineo**_\n"
                "**#AllieRemembers 🧠**"
            ),
            color=discord.Color.dark_purple()
        )

        await channel.send(embed=embed)
        await channel.send("@everyone")  # 🔔 Notify everyone about the update
        await ctx.send("✅ Update v1.0.2 posted successfully!")

async def setup(bot):
    await bot.add_cog(Setup(bot))
