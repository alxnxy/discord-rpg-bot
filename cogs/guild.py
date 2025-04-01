class GuildSystem(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    @commands.command()
    async def create_guild(self, ctx, name: str):
        self.db.create_guild(ctx.author.id, name)
        await ctx.send(f"Guild {name} berhasil dibuat!")
