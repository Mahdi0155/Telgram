from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

router = Router()

# کیبورد انتخاب درس
def study_subjects_keyboard():
    keyboard = [
        [KeyboardButton(text="ریاضی"), KeyboardButton(text="فیزیک")],
        [KeyboardButton(text="شیمی"), KeyboardButton(text="زیست")],
        [KeyboardButton(text="ادبیات"), KeyboardButton(text="دین و زندگی")],
        [KeyboardButton(text="برگشت به منو اصلی")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

# هندلر برای باز شدن بخش نحوه مطالعه
@router.message(lambda message: message.text == "نحوه مطالعه")
async def show_study_menu(message: Message):
    await message.answer("درس مورد نظرت رو انتخاب کن:", reply_markup=study_subjects_keyboard())

# هندلر برای پاسخ به انتخاب درس
@router.message(lambda message: message.text in ["ریاضی", "فیزیک", "شیمی", "زیست", "ادبیات", "دین و زندگی"])
async def study_subject(message: Message):
    subject = message.text

    responses = {
        "ریاضی": "برای موفقیت در ریاضی، تمرین مستمر و حل تست‌های مختلف بسیار مهمه. هر روز زمان مشخصی رو به ریاضی اختصاص بده.",
        "فیزیک": "در فیزیک، مفاهیم پایه‌ای مثل نیرو و حرکت رو خوب بفهم، بعد برو سراغ فرمول‌ها. حل مسئله کلید موفقیته.",
        "شیمی": "شیمی نیاز به حفظ کردن مفاهیم داره، ولی حتماً بعدش تست کار کن که تثبیت بشه. معادله‌های واکنش رو کامل یاد بگیر.",
        "زیست": "زیست حفظیه ولی مفهومی حفظ کن. سعی کن مطالب رو با هم ارتباط بدی تا راحت‌تر یادت بمونه.",
        "ادبیات": "ادبیات ترکیبی از حفظ شعر و فهم آرایه‌هاست. لغت و تاریخ ادبیات رو روزانه مرور کن.",
        "دین و زندگی": "دین و زندگی بیشتر مفهومی شده. پیام آیات رو دقیق بخون و مفهوم‌شون رو درک کن."
    }

    await message.answer(responses[subject])

# هندلر برگشت به منو اصلی
@router.message(lambda message: message.text == "برگشت به منو اصلی")
async def back_to_main_menu(message: Message):
    from keyboards.reply import main_menu_keyboard
    await message.answer("برگشتی به منوی اصلی:", reply_markup=main_menu_keyboard())
