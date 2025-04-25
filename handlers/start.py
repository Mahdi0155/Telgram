from aiogram import Router, F
from aiogram.types import Message
from keyboards.reply import main_menu_keyboard
from db import get_user

router = Router()

@router.message(F.text == "/start")
async def start_command(message: Message):
    user_id = message.from_user.id
    user = get_user(user_id)

    if user:
        await message.answer(
            f"سلام دوباره {user[1]}! خوش اومدی به ربات مشاوره‌ای ما! {chr(0x1F389)}\n\n"
            "از منوی زیر استفاده کن:",
            reply_markup=main_menu_keyboard()
        )
    else:
        await message.answer(
            f"سلام! به ربات مشاوره‌ای خوش اومدی! {chr(0x1F4DA)}\n"
            "بیا اول یه پروفایل برات بسازیم تا بتونی از امکانات ربات استفاده کنی:",
            reply_markup=main_menu_keyboard()
        )
        from handlers import profile
        await profile.start_registration(message)
