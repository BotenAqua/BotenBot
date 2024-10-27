from discord.ext import commands


class ExampleCogModule(commands.Cog):
    def __init__(self):
        print('ExampleCogModule loaded successfully!')
        return


async def setup(bot):
    await bot.add_cog(ExampleCogModule())
