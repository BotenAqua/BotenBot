from discord.ext import commands


class ExampleCog(commands.Cog):
    def __init__(self):
        print('ExampleCog loaded successfully!')
        return


async def setup(bot):
    await bot.add_cog(ExampleCog())
