class PVPSystem(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    @commands.command()
    async def duel(self, ctx, opponent: discord.Member):
        await ctx.send(f"Duel request sent to {opponent.mention}!")
