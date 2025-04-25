from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from keyboards.reply import main_menu_keyboard
from db import get_user

router = Router()

@router.message(F.text == "/start")
async def start_command(message: Message, state: FSMContext):
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
        await start_registration(message, state)

async def start_registration(message: Message, state: FSMContext):
    await message.answer("ثبت نام شروع شد! لطفا اطلاعاتتو وارد کن...")
