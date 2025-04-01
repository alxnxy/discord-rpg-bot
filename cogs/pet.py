class PetSystem(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    @commands.command()
    async def pet(self, ctx):
        pet = self.db.get_pet(ctx.author.id)
        await ctx.send(f"Your pet: {pet['name']} (Level {pet['level']})")
