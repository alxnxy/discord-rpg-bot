
class CraftingSystem(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    @commands.command()
    async def craft(self, ctx, item: str):
        recipe = self.db.recipes.get(item)
        if not recipe:
            await ctx.send("Item tidak ditemukan!")
            return
        # Logika crafting
