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
            title="🚀 Marra Update Log - v1.0.0",
            description=(
                "**Greetings, DevLab explorers! 🧪**\n"
                "Marra has officially gone online. This marks the beginning of an intelligent assistant designed for **AI development, programming collaboration, and game dev support**.\n\n"
                "---\n"
                "**🧠 Core Features Now Live:**\n"
                "✅ Auto role assignment: 🧠 Curious Coder for newcomers\n"
                "✅ Moderation tools: `!kick`, `!ban` (authorized access only)\n"
                "✅ Global command lock to prevent spam or misuse\n"
                "✅ Hidden command activity for clean channels\n"
                "✅ Welcome system with embedded onboarding message\n\n"
                "---\n"
                "**🧭 Coming Soon:**\n"
                "⚙️ Reaction-based role system\n"
                "🤖 Allie protocol: AI conversational assistant\n"
                "🧾 Server stats & info commands\n"
                "🔒 Permission-aware utilities\n\n"
                "_Developed and maintained by **Marineo**_\n"
                "**#MarraRising 🌌**"
            ),
            color=discord.Color.teal()
        )

        await channel.send(embed=embed)
        await ctx.send("✅ Update posted successfully!")

async def setup(bot):
    await bot.add_cog(Setup(bot))
