import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.kick(reason=reason)
            await ctx.send(f"👢 {member} has been kicked. Reason: {reason or 'No reason provided.'}")
        except discord.Forbidden:
            await ctx.send("❌ I don't have permission to kick this member.")
        except Exception:
            pass  # Fully silent fallback

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.ban(reason=reason)
            await ctx.send(f"🔨 {member} has been banned. Reason: {reason or 'No reason provided.'}")
        except discord.Forbidden:
            await ctx.send("❌ I don't have permission to ban this member.")
        except Exception:
            pass  # Fully silent fallback

    # ❌ REMOVE custom error handlers like @kick.error — we'll handle all errors in Marra.py

async def setup(bot):
    await bot.add_cog(Moderation(bot))
