from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from db import get_user, remove_coins
from config import ADMIN_ID  # تو این فایل آیدی خودتو می‌ذاری
from keyboards.reply import main_menu_keyboard

router = Router()

class Ask(StatesGroup):
    waiting_for_question = State()

# شروع پرسش
@router.message(F.text == "سوال مشاوره‌ای 🧠")
async def start_ask(message: Message, state: FSMContext):
    user = get_user(message.from_user.id)

    if not user or user[9] < 1:
        await message.answer("برای پرسیدن سوال باید حداقل ۱ سکه داشته باشی.")
        return

    await message.answer("سوالتو بنویس، تا برای مشاور فرستاده بشه:")
    await state.set_state(Ask.waiting_for_question)

# دریافت سوال
@router.message(Ask.waiting_for_question)
async def receive_question(message: Message, state: FSMContext):
    question = message.text
    user = get_user(message.from_user.id)

    if not user or user[9] < 1:
        await message.answer("سکه‌هات تموم شده. نمی‌تونی سوال بفرستی.")
        await state.clear()
        return

    remove_coins(message.from_user.id, 1)

    await message.answer("سوالت با موفقیت ارسال شد! منتظر پاسخ بمون.", reply_markup=main_menu_keyboard())

    await message.bot.send_message(
        ADMIN_ID,
        f"سوال جدید از {user[2]} (@{user[8]}):\n\n{question}"
    )

    await state.clear()
