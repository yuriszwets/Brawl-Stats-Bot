import asyncio
import logging
import os
import sys

import aiohttp
from aiogram import Bot, Dispatcher, F, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import BotCommand, BufferedInputFile, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    sys.exit("BOT_TOKEN is missing. Add it to your .env file.")

dp = Dispatcher()

PLAYER_TAG = "92CCUP828"
BASE_URL = "https://img.sltbot.com/player/{tag}/{stat}?o=h"

STATS = {
    "battles": "⚔️ Battles",
    "winstreaks": "🔥 Win streaks",
    "wsmax": "🏆 Max win streak",
    "powers": "⚡ Powers",
    "brawlers_legacy": "🧬 Brawlers legacy",
    "trophies": "🏅 Trophies",
    "trmax": "📈 Max trophies",
    "ranks": "🎖 Ranks",
    "ranks_50": "🎖 Ranks 50",
    "ranks_legacy": "🎖 Ranks legacy",
    "mastery": "🧠 Mastery",
    "mastery_points": "💠 Mastery points",
}


def stats_keyboard():
    builder = InlineKeyboardBuilder()
    for key, label in STATS.items():
        builder.button(text=label, callback_data=f"stat:{key}")
    builder.adjust(2)
    return builder.as_markup()


@dp.message(CommandStart())
async def start_handler(message: types.Message) -> None:
    await message.answer(
        "Hi! Welcome to the Brawl Stars Account Photo Bot!\n\n"
        "Here you can get a photo of your Brawl Stars account. "
        "Just use the available commands to get started.\n\n"
        "Use /help to see all available commands."
    )


@dp.message(Command("help"))
async def help_handler(message: types.Message) -> None:
    await message.answer(
        "Commands available:\n"
        "/start - Start the bot\n"
        "/help - Get help\n"
        "/brawlify - View statistics"
    )


@dp.message(Command("brawlify"))
async def brawlify_handler(message: types.Message) -> None:
    await message.answer("Select a stat:", reply_markup=stats_keyboard())


@dp.callback_query(F.data.startswith("stat:"))
async def stat_handler(callback: CallbackQuery) -> None:
    stat = callback.data.split(":", 1)[1]
    if stat not in STATS:
        await callback.answer("Unknown stat", show_alert=True)
        return

    await callback.answer("Processing 🕙")

    url = BASE_URL.format(tag=PLAYER_TAG, stat=stat)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=20)) as resp:
                if resp.status != 200:
                    await callback.message.answer("Couldn't load that image, try again later.")
                    return
                data = await resp.read()
    except (aiohttp.ClientError, asyncio.TimeoutError):
        await callback.message.answer("Image server is not responding, try again later.")
        return

    photo = BufferedInputFile(data, filename=f"{stat}.png")
    await callback.message.answer_photo(photo, caption=STATS[stat])



async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    main_commands = [
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="help", description="Get help"),
        BotCommand(command="brawlify", description="View statistics"),
    ]
    await bot.set_my_commands(main_commands)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())