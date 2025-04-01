class AdminCommands(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    @commands.command()
    @commands.is_owner()
    async def resetuser(self, ctx, user: discord.Member):
        self.db.reset_user(user.id)
        await ctx.send(f"User {user.name} berhasil direset!")
