import os


async def _load_cog(bot, cog_name) -> None:
    if cog_name in ['__pycache__']:
        return
    if (cog := f'cogs.{cog_name.removesuffix(".py")}') not in bot.extensions.keys():
        await bot.load_extension(cog)
    return

async def load_cogs(bot) -> None:
    # TODO: Try to add this
    # cogs_location = os.getenv('COGS_LOCATION', os.path.join(bot.bot_dir, '../cogs'))
    cogs_location = '../cogs'
    cogs_list = os.listdir(os.path.join(bot.bot_dir, cogs_location))

    if len(cogs_list) == 0:
        print(bot.lang.get('cogs_dir_empty'))
        return

    prioroty_cogs = os.getenv('PRIORITY_COGS', list()).split() # TODO: ,? ', '?

    if type(prioroty_cogs) != list:
        print(bot.lang.get('priority_cogs_error'))
    else:
        for cog in prioroty_cogs:
            try:
                await _load_cog(bot, cog)
            except Exception as e:
                # TODO: Add this
                # print(f"{bot.lang.get('cog_load_error')}")
                print(f'There was an error loading {cog} cog: {e}')

    for filename in cogs_list:
        await _load_cog(bot, filename)
    return
