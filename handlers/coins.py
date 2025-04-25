# handlers/coins.py

from aiogram import Router, types
from database import db

router = Router()

@router.message(commands=["coins", "سکه"])
async def show_coins(message: types.Message):
    user = db.get_user(message.from_user.id)
    if user:
        coins = user[-1]  # آخرین ستون دیتابیس سکه است
        await message.answer(f"تعداد سکه‌های شما: {coins} 🪙")
    else:
        await message.answer("شما ثبت‌نام نکردید. لطفاً اول ثبت‌نام کنید.")
