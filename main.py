import os
from aiogram import Bot, Dispatcher, executor, types
from db import create_tables, get_session, User
from config import ADMIN_ID

# توکن ربات از محیط یا مستقیم
BOT_TOKEN = os.getenv('BOT_TOKEN')  # روی رندر باید ENV بسازی به اسم BOT_TOKEN
if not BOT_TOKEN:
    BOT_TOKEN = 'اینجا توکن رباتتو بذار'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# ساختن دیتابیس
create_tables()

# شروع ربات
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    session = get_session()
    user = session.query(User).filter_by(id=message.from_user.id).first()

    if not user:
        new_user = User(
            id=message.from_user.id,
            username=message.from_user.username,
            coins=5,  # سکه اولیه مثلا
            grade="",
            major="",
            province="",
            city=""
        )
        session.add(new_user)
        session.commit()
        await message.answer("سلام! ثبت‌نامت انجام شد!")
    else:
        await message.answer("قبلا ثبت‌نام کردی!")

    session.close()

# تست پیام ساده
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer("دستورات موجود:\n/start - شروع\n/help - راهنما")

# اجرای ربات
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
