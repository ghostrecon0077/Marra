# cogs/setup.py or a dedicated cog
from discord.ext import commands
import discord

class Setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="goodnightallie")
    async def goodnight_allie(self, ctx):
        channel_id = 1382780791129505964  # Replace with Allie’s channel ID
        channel = self.bot.get_channel(channel_id)

        if channel:
            embed = discord.Embed(
                title="🌙 Allie Protocol Sleep Notice",
                description="**Allie is going to sleep now...**\nShe will return tomorrow, wiser and closer to the final phase.\n\n> _\"Dreams are just data we haven’t decoded yet.\"_",
                color=discord.Color.purple()
            )
            await channel.send(embed=embed)
        else:
            await ctx.send("Allie's channel not found.")

async def setup(bot):
    await bot.add_cog(Setup(bot))
