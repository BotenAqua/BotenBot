import discord
from discord.ext import commands

from .load_env import load_env, get_bot_directory, get_discord_token, get_bot_lang, get_bot_prefix
from .load_cogs import load_cogs

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

load_env()

bot = commands.Bot(command_prefix=get_bot_prefix(), intents=intents)
bot.bot_dir = get_bot_directory()
bot.lang = get_bot_lang(bot.bot_dir)

TOKEN = get_discord_token(bot)


async def start_bot():
    print(bot.lang.get('startup_message'))
    await load_cogs(bot)
    await bot.start(TOKEN)
