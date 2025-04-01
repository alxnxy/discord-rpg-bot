class DungeonSystem(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    @commands.command()
    async def enter_dungeon(self, ctx, name: str):
        await ctx.send(f"Entering dungeon: {name}")
