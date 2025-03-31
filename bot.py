import discord
from discord.ext import commands
import config
from database import Database

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
db = Database()

async def load_cogs():
    await bot.add_cog(RPGSystem(bot, db))
    await bot.add_cog(BattleSystem(bot, db))
    await bot.add_cog(PetSystem(bot, db))
    await bot.add_cog(EconomySystem(bot, db))
    await bot.add_cog(CraftingSystem(bot, db))
    await bot.add_cog(GuildSystem(bot, db))
    await bot.add_cog(AdminCommands(bot, db))
    await bot.add_cog(QuestSystem(bot, db))
    await bot.add_cog(AchievementSystem(bot, db))
    await bot.add_cog(PVPSystem(bot, db))
    await bot.add_cog(DungeonSystem(bot, db))
    await bot.add_cog(HousingSystem(bot, db))
    await bot.add_cog(TransmogSystem(bot, db))
    await bot.add_cog(DynamicSystem(bot, db))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await load_cogs()

if __name__ == "__main__":
    bot.run(config.TOKEN)
