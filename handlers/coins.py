from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import db  # اصلاح شد

router = Router()

@router.message(Command("coins"))
async def show_coins(message: Message):
    user = db.get_user(message.from_user.id)
    if user:
        coins = user[-1]  # مقدار coins در ستون آخر جدول
        await message.answer(f"تعداد سکه‌های شما: {coins} 🪙")
    else:
        await message.answer("شما هنوز ثبت‌نام نکردید. لطفاً ابتدا ثبت‌نام کنید.")

@router.message(F.text == "دریافت سکه رایگان")
async def free_coins_menu(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="عضویت در کانال (۵ سکه)")],
            [KeyboardButton(text="دعوت دوستان")],
            [KeyboardButton(text="بازگشت")]
        ],
        resize_keyboard=True
    )
    await message.answer("یکی از روش‌های دریافت سکه رایگان رو انتخاب کن:", reply_markup=keyboard)
