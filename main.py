import discord
from discord.ext import commands
import config
from commands import kick, ban, unban, clear, setrole

token = config.token

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    bot.load_extension('cogs.commands')

bot.run(token)