# BotenBot

Simple [Dockerized](https://hub.docker.com/r/botenaqua/discord-botenbot/tags) Discord.py bot.

## Table of contents

- [General Info](#general-info)
- [Technologies](#technologies)
- [Setup](#setup)
- [Features](#features)
- [Status](#status)

## General info

BotenBot is a simple Discord bot using [Discord.py](https://github.com/Rapptz/discord.py). This is a refactor of my private bot repo with too many hardcoded me-specific lines. This revision will be Dockerized, customisable, and easy to use with little to no knowledge.

## Technologies

discord.py==2.4.0

## Setup

The bot takes environmental variables:

```bash
DISCORD_TOKEN=XXXXXXXXXXXXXX...

DOTENV_PATH=path/to/.env

BOT_LANG=[en | pl]
BOT_PREFIX=
PRIORITY_COGS='cog1 cog2...'
```
### DISCORD_TOKEN
*(required)*

Discord token is required for bot to run. App will close if not provided.

### DOTENV_PATH

Path to .env file.

### BOT_LANG

Desired language to get correct prints from bot/text_langs.json file. If not provided or provided language will not be found, defaults to English.

Avaliable languages:
```
en -> English
pl -> Polish
```

### BOT_PREFIX

Bot prefix. Default: '!'

### PRIORITY_COGS

Space separated list of cogs that should be loaded before the rest.

---

You can start the bot by running main.py
```bash
python main.py
```

## Features

BotenBot is a Discord bot with a `cogs` folder replaceable with Docker volume `-v path/to/your/cogs:/cogs` to simplify cog development without changing the core app.

To do:

- [x] Dockerize
- [x] QOL (changeable command_prefix etc.)
- [x] Localization support
- [ ] Debug mode
- [ ] Logger (\*)
- [ ] Database (\*)
- [ ] Web-based UI (\*)
- [ ] .yml config (\*)
- [ ] Setup run `--setup` (\*)
- [ ] more example cogs (\*)

\* might be rejected to keep the project as simple as possible to give users all the control.

## Status

The project is currently **in development**.
