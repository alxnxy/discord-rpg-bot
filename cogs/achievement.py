class AchievementSystem(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    @commands.command()
    async def achievements(self, ctx):
        achievements = self.db.get_achievements(ctx.author.id)
        await ctx.send(f"Unlocked: {', '.join(achievements)}")
