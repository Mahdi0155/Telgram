import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties
from handlers import start, profile, percent, study, coins, ask_question
from admin import panel
from dotenv import load_dotenv
from db import init_db

# Load environment variables
load_dotenv()

# Initialize bot and dispatcher
bot = Bot(
    token=os.getenv("BOT_TOKEN"),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

# Register routers
dp.include_routers(
    start.router,
    profile.router,
    percent.router,
    study.router,
    coins.router,
    ask_question.router,
    panel.router,
)

async def main():
    init_db()
    print("ربات آماده است...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
