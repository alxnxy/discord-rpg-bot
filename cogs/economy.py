class EconomySystem(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    @commands.command()
    async def balance(self, ctx):
        user = self.db.get_user(ctx.author.id)
        await ctx.send(f"Gold: {user['gold']} | Gems: {user['gems']}")
