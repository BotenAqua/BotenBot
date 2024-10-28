import os


async def load_cogs(bot) -> None:
    cogs_location = './cogs'
    cogs_list = os.listdir(cogs_location)

    if len(cogs_list) == 0:
        print(bot.lang.get('cogs_dir_empty'))
        return

    for filename in cogs_list:
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
        elif os.path.isdir(os.path.join(os.path.abspath(cogs_location), filename))\
                and filename != '__pycache__':
            await bot.load_extension(f'cogs.{filename}')

    return
