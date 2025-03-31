class BattleSystem(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    @commands.command()
    async def hunt(self, ctx):
        monster = random.choice(self.db.monsters)
        await ctx.send(f"You encountered a {monster['name']}! Use `!attack` to fight!")
