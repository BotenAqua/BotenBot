# BotenBot

Simple (to be) Dockerized Discord.py bot.

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

The bot takes two environmental variables:

DISCORD_TOKEN
```bash
DISCORD_TOKEN=XXXXXXXXXXXXXX...
```
DOTENV_PATH
```bash
DOTENV_PATH='path/to/.env'
```
Only the token is required, but it can be in the .env file if the path to it is specified.

You can start the bot by running main.py
```bash
python main.py
```

## Features

BotenBot is a Discord bot with a `cogs` folder replaceable with Docker volume `-v path/to/your/cogs:/cogs` to simplify cog development without changing the core app.

To do:

- [ ] Dockerize
- [ ] QOL (changeable command_prefix etc.)
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
