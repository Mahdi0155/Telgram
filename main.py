from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
import asyncio
import logging

from config import BOT_TOKEN
from handlers import profile  # هندلرهایی که ساختی
from db import create_tables

# فعال‌سازی لاگ‌ها
logging.basicConfig(level=logging.INFO)

# راه‌اندازی ربات
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# افزودن هندلرها
dp.include_router(profile.router)

# تعریف دستورات پیش‌فرض
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="شروع ربات"),
    ]
    await bot.set_my_commands(commands)

# تابع اصلی اجرا
async def main():
    await set_commands(bot)
    create_tables()  # ساخت جدول‌های دیتابیس
    await dp.start_polling(bot)

if __name__ == "__main__":
    import threading
    import os
    from http.server import BaseHTTPRequestHandler, HTTPServer

    # اجرای سرور فیک برای رفع مشکل Render
    class SimpleHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Bot is running')

    def run_fake_server():
        port = int(os.environ.get("PORT", 8080))
        server = HTTPServer(("0.0.0.0", port), SimpleHandler)
        server.serve_forever()

    # اجرای سرور فیک در یک ترد جدا
    threading.Thread(target=run_fake_server).start()

    # اجرای اصلی ربات
    asyncio.run(main())
