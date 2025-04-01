class QuestSystem(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    @commands.command()
    async def quest(self, ctx):
        quests = self.db.get_quests(ctx.author.id)
        await ctx.send(f"Active quests: {', '.join(quests)}")
