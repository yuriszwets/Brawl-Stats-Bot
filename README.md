# Brawl Stars Bot

Telegram bot that sends images of Brawl Stars account stats (trophies, win streaks, mastery and more), so you don't have to look them up on the web.

## Commands

| Command | Description |
| --- | --- |
| `/start` | Start the bot |
| `/help` | List available commands |
| `/brawlify` | Open the stats menu and pick a stat |

## Available stats

Battles, win streaks, max win streak, powers, brawlers legacy, trophies, max trophies, ranks, ranks 50, ranks legacy, mastery, mastery points.

## Quick start

Requires Python 3.10+ and a bot token from [@BotFather](https://t.me/BotFather).

```bash
git clone https://github.com/<user>/<repo>.git
cd <repo>
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # then put your token in .env
python bot.py
```

## Configuration

| Variable | Required | Description |
| --- | --- | --- |
| `BOT_TOKEN` | yes | Token from @BotFather |
| `PLAYER_TAG` | no | Player tag without `#` (currently set in code) |

## How it works

1. The user sends `/brawlify`, and the bot replies with an inline keyboard of stats.
2. On button press, the bot downloads the stat image from `img.sltbot.com` and sends it back as a photo.
3. If the image server fails or times out (20 s), the user gets an error message.

Built with [aiogram 3](https://docs.aiogram.dev/) and aiohttp.

## Project structure

```
bot.py             # handlers and startup
requirements.txt
.env.example
```

## License

MIT