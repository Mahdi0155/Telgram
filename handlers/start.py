# handlers/start.py
from aiogram import Router, F
from aiogram.types import Message
from keyboards.reply import main_menu_keyboard
from db import get_user

# اینو برای شروع ثبت‌نام می‌اریم از profile
from handlers import profile

router = Router()

@router.message(F.text == "/start")
async def start_command(message: Message):
    user_id = message.from_user.id
    user = get_user(user_id)

    if user:
        await message.answer(
            f"سلام دوباره {user[1]}! خوش اومدی به ربات مشاوره‌ای ما! 🎉\n\n"
            "از منوی زیر استفاده کن:",
            reply_markup=main_menu_keyboard()
        )
    else:
        await message.answer(
            "سلام! به ربات مشاوره‌ای خوش اومدی! 📚\n"
            "بیا اول یه پروفایل برات بسازیم تا بتونی از امکانات ربات استفاده کنی:"
        )
        await profile.start_registration(message)
