import os
import sys
import json

from dotenv import load_dotenv


def load_env() -> None:
    if _dotenv_path := os.getenv('DOTENV_PATH'):
        load_dotenv(_dotenv_path)
    return


def get_discord_token(bot) -> str:
    if not (discord_token := os.getenv('DISCORD_TOKEN')):
        print(bot.lang.get('discord_token_missing'))
        sys.exit(0)
    return discord_token


def get_bot_lang() -> dict:
    dict_file_location = 'bot/text_langs.json'
    lang = os.getenv('BOT_LANG') or 'en'
    with open(dict_file_location) as lang_file:
        lang_dict = json.load(lang_file)
    if not (lang in lang_dict):
        print(f'Language you provided ({lang}) is not in {dict_file_location} file. Using default English.')
        lang = 'en'
    return lang_dict[lang]


def get_bot_prefix() -> str:
    return os.getenv('BOT_PREFIX') or '!'
