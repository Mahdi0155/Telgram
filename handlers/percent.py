from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message(lambda message: message.text.lower() == "درصدگیری")
async def calculate_percent(message: Message):
    await message.answer(
        "برای محاسبه درصد، تعداد پاسخ‌های درست و تعداد کل سوالات رو به این صورت بفرست:\n\n"
        "<code>درست/کل</code>\n\n"
        "مثال: 18/20"
    )

@router.message(lambda message: "/" in message.text and message.text.count("/") == 1)
async def show_percent(message: Message):
    try:
        correct, total = map(int, message.text.split("/"))
        if total == 0:
            await message.answer("تعداد کل سوالات نباید صفر باشه.")
            return
        percent = (correct / total) * 100
        await message.answer(f"درصدت: {percent:.2f}%")
    except:
        await message.answer("فرمت ورودی اشتباهه. مثال صحیح: 18/20")
