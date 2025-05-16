import os


async def _load_cog(bot, cog_name) -> None:
    if cog_name in ['__pycache__']:
        return
    if (cog := f'cogs.{cog_name.removesuffix(".py")}') not in bot.extensions.keys():
        await bot.load_extension(cog)
    return

async def _cog_loader(bot, cogs_location, cogs_list):
    if len(cogs_list) == 0:
        print(bot.lang.get('cogs_dir_empty'))
        return

    for cog in cogs_list:
        try:
            await _load_cog(bot, cog)
        except Exception as e:
            # TODO: Add this
            # print(f"{bot.lang.get('cog_load_error')}")
            print(f'There was an error loading {cog} cog: {e}')
    return 

async def required_cogs(bot, *required_cogs):
    # TODO: Try to add this
    # cogs_location = os.getenv('COGS_LOCATION', os.path.join(bot.bot_dir, '../cogs'))
    # code duplication!!
    cogs_location = '../cogs'
    print(required_cogs)
    await _cog_loader(bot, cogs_location, required_cogs)
    return

async def load_cogs(bot) -> None:
    # TODO: Try to add this
    # cogs_location = os.getenv('COGS_LOCATION', os.path.join(bot.bot_dir, '../cogs'))
    cogs_location = '../cogs'
    cogs_list = os.listdir(os.path.join(bot.bot_dir, cogs_location))

    await _cog_loader(bot, cogs_location, cogs_list)

    return
