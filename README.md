# DiscordBot

A simple interactive Discord bot built with Python and discord.py.

## Features

- **`!hello`** - Bot greets you
- **`!story`** - Start a random interactive story
- **`!choose`** - Make choices in your story (`left` or `right`)
- **`!chat`** - Chat with the bot (try "hello", "python", or "discord")

## Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) package manager
- Discord bot token

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd DiscordBot
```

2. Install dependencies:
```bash
uv sync
```

3. Create a `.env` file in the root directory:
```env
DISCORD_TOKEN=your_bot_token_here
```

4. Run the bot:
```bash
uv run bot.py
```

## Discord Bot Setup

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application and bot
3. Enable "Message Content Intent" under Bot settings
4. Copy the bot token to your `.env` file
5. Invite the bot using OAuth2 URL with `bot` scope

## Project Structure

```
DiscordBot/
├── bot.py              # Main bot file
├── commands/
│   ├── hello.py        # Hello command
│   ├── story.py        # Story command logic
│   ├── choose.py       # Choice command logic
│   └── chat.py         # Chat responses
├── choises/
│   └── story.py        # Story data (locations, items, events)
├── src/
│   └── discordbot/     # Package module
├── pyproject.toml      # Project configuration
└── .env                # Environment variables (not committed)
```

## License

MIT
