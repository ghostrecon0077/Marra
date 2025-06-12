import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # ✅ Auto-assign 🧠 Curious Coder role
        role = discord.utils.get(member.guild.roles, name="🧠 Curious Coder")
        if role:
            try:
                await member.add_roles(role)
                print(f"[AUTO ROLE] Assigned '🧠 Curious Coder' to {member.name}")
            except discord.Forbidden:
                print("[ERROR] Missing permission to assign '🧠 Curious Coder' role")
            except Exception as e:
                print(f"[ROLE ERROR] {e}")
        else:
            print("[ERROR] Role '🧠 Curious Coder' not found")

        # ✅ Send welcome embed message
        try:
            channel = discord.utils.get(member.guild.text_channels, name="welcome")
            if not channel:
                print("[ERROR] Channel named 'welcome' not found")
                return

            embed = discord.Embed(
                title=f"👋 Welcome to {member.guild.name}!",
                description=(
                    f"Hello {member.mention}, I'm **Marra**, an intelligent AI assistant developed by **Marineo**.\n\n"
                    "Welcome to **Marineo's DevLab** — a community of passionate minds building in **AI, programming, game dev, and bots**.\n\n"
                    "🎯 Collaborate, learn, and bring your ideas to life here.\n"
                    "Don't forget to check out the rules and pick your roles!"
                ),
                color=discord.Color.purple()
            )
            embed.set_footer(text="Glad to have you with us 💫")

            await channel.send(embed=embed)
            print(f"[WELCOME] Sent welcome message for {member.name}")

        except discord.Forbidden:
            print("[ERROR] Missing permission to send messages in #welcome")
        except Exception as e:
            print(f"[WELCOME ERROR] {e}")

# ✅ Setup function
async def setup(bot):
    await bot.add_cog(Welcome(bot))
