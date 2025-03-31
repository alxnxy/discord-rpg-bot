import discord
from discord.ext import commands
from database import Database

class RPGSystem(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    @commands.command()
    async def profile(self, ctx):
        user = self.db.get_user(ctx.author.id)
        embed = discord.Embed(title=f"{ctx.author}'s Profile")
        embed.add_field(name="Level", value=user['level'])
        embed.add_field(name="HP", value=f"{user['hp']}/{user['max_hp']}")
        await ctx.send(embed=embed)
