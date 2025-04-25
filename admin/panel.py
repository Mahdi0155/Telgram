from aiogram import Router, F
from aiogram.types import Message
from db import get_unanswered_questions, answer_question

router = Router()

ADMIN_ID = 6387942633  # آیدی عددی تلگرام ادمین

@router.message(F.text == "پنل ادمین")
async def admin_panel(message: Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("شما دسترسی به پنل ادمین ندارید.")
        return

    questions = get_unanswered_questions()
    if not questions:
        await message.answer("هیچ سوال بی‌پاسخی وجود ندارد.")
        return

    response = "سوالات بدون پاسخ:\n\n"
    for q in questions:
        response += f"آیدی سوال: {q[0]}\nسوال: {q[1]}\n\n"

    await message.answer(response)

@router.message(F.text.startswith("پاسخ "))
async def answer_to_question(message: Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("شما دسترسی به پنل ادمین ندارید.")
        return

    try:
        parts = message.text.split(' ', 2)
        question_id = int(parts[1])
        answer_text = parts[2]
    except (IndexError, ValueError):
        await message.answer("فرمت درست: پاسخ [آیدی سوال] [متن پاسخ]")
        return

    success = answer_question(question_id, answer_text)
    if success:
        await message.answer("پاسخ با موفقیت ثبت شد.")
    else:
        await message.answer("مشکلی پیش آمد یا سوال پیدا نشد.")
