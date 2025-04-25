from aiogram import Router, types
from db import get_all_unanswered_questions, answer_question, mark_question_as_answered

router = Router()

ADMIN_ID = 6387942633  # آیدی تلگرام ادمین اصلی

@router.message(lambda message: message.from_user.id == ADMIN_ID and message.text == "/admin")
async def admin_panel(message: types.Message):
    questions = get_all_unanswered_questions()
    if not questions:
        await message.answer("هیچ سوال پاسخ داده نشده‌ای وجود ندارد.")
        return

    for q in questions:
        question_id, user_id, question_text = q
        await message.answer(f"سوال #{question_id} از کاربر {user_id}:\n\n{question_text}")

@router.message(lambda message: message.from_user.id == ADMIN_ID and message.text.startswith("جواب"))
async def send_answer(message: types.Message):
    try:
        _, qid, *answer_parts = message.text.split()
        qid = int(qid)
        answer_text = " ".join(answer_parts)
    except Exception as e:
        await message.answer("فرمت پاسخ اشتباهه. باید اینطوری باشه:\nجواب [ایدی سوال] [متن پاسخ]")
        return

    user_id = answer_question(qid, answer_text)
    if user_id:
        await message.bot.send_message(user_id, f"پاسخ سوال شما:\n{answer_text}")
        mark_question_as_answered(qid)
        await message.answer("✅ پاسخ ارسال شد.")
    else:
        await message.answer("❌ سوال پیدا نشد یا قبلاً پاسخ داده شده.")
