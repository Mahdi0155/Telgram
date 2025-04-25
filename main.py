import logging
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN, ADMIN_ID
from db import create_tables, Session, User

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# ساخت جدول‌ها
create_tables()

# دکمه‌های منو
def main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("پروفایل من", "دریافت سکه")
    return keyboard

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    session = Session()
    user = session.query(User).filter_by(user_id=message.from_user.id).first()
    if not user:
        new_user = User(
            user_id=message.from_user.id,
            username=message.from_user.username,
            coins=5  # سکه اولیه
        )
        session.add(new_user)
        session.commit()
        await message.answer("ثبت‌نام با موفقیت انجام شد!", reply_markup=main_menu())
    else:
        await message.answer("قبلاً ثبت‌نام کردی!", reply_markup=main_menu())
    session.close()

# هندل دکمه‌ها
@dp.message_handler(lambda msg: msg.text == "پروفایل من")
async def profile(message: types.Message):
    session = Session()
    user = session.query(User).filter_by(user_id=message.from_user.id).first()
    session.close()
    if user:
        await message.answer(f"نام کاربری: @{user.username}\nسکه‌ها: {user.coins}")
    else:
        await message.answer("شما هنوز ثبت‌نام نکردید.")

@dp.message_handler(lambda msg: msg.text == "دریافت سکه")
async def get_coins(message: types.Message):
    await message.answer("برای دریافت سکه باید دوستانتو دعوت کنی یا عضو کانال بشی (در آینده فعال میشه).")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
