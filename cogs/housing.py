class HousingSystem(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    @commands.command()
    async def buyhouse(self, ctx):
        await ctx.send("Rumah berhasil dibeli!")
