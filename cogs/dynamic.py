class DynamicSystem(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    @commands.command()
    async def weather(self, ctx):
        await ctx.send("Cuaca saat ini: Cerah")
