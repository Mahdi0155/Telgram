from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from db import get_user, remove_coins
from config import ADMIN_ID
from keyboards.reply import main_menu_keyboard

router = Router()

class AskState(StatesGroup):
    waiting_for_question = State()

@router.message(F.text == "❓ رفع اشکال")
async def ask_question(message: Message, state: FSMContext):
    user = get_user(message.from_user.id)
    if not user:
        await message.answer("لطفاً اول ثبت‌نام کن!")
        return

    coins = user[-1]  # آخرین مقدار توی دیتا، سکه‌هاست
    if coins < 1:
        await message.answer("برای پرسیدن سؤال باید حداقل ۱ سکه داشته باشی!")
        return

    await message.answer("سؤالتو بفرست تا به مشاور ارسال بشه:")
    await state.set_state(AskState.waiting_for_question)

@router.message(AskState.waiting_for_question)
async def receive_question(message: Message, state: FSMContext):
    user = get_user(message.from_user.id)
    question = message.text

    remove_coins(message.from_user.id, 1)

    await message.answer("سؤالت ارسال شد! منتظر پاسخ مشاور باش.", reply_markup=main_menu_keyboard())

    text = f"❓ <b>سؤال جدید از کاربر:</b>\n\n" \
           f"🧑‍🎓 <b>نام:</b> {user[2]}\n" \
           f"📚 <b>رشته:</b> {user[4]}\n" \
           f"🎓 <b>پایه:</b> {user[3]}\n" \
           f"📍 <b>شهر:</b> {user[6]} ({user[5]})\n" \
           f"🆔 <b>یوزرنیم:</b> @{user[7]}\n\n" \
           f"✏️ <b>سؤال:</b>\n{question}"

    await message.bot.send_message(chat_id=ADMIN_ID, text=text)
    await state.clear()
