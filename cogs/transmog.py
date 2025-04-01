class TransmogSystem(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    @commands.command()
    async def transmog(self, ctx, item: str):
        await ctx.send(f"Item {item} berhasil diubah tampilannya!")
