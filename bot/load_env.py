import os
import sys

from dotenv import load_dotenv


def load_env():
    if _dotenv_path := os.getenv('DOTENV_PATH'):
        load_dotenv(_dotenv_path)
    return


def get_discord_token():
    if not (_discord_token := os.getenv('DISCORD_TOKEN')):
        print('Discord token was not found! Exiting...')
        sys.exit(0)
    return _discord_token
