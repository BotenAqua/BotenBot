import discord
from discord.ext import commands

from .load_env import load_env, get_discord_token
from .load_cogs import load_cogs

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

load_env()
TOKEN = get_discord_token()


async def start_bot():
    print('BotenBot is starting...')
    await load_cogs(bot)
    await bot.start(TOKEN)
