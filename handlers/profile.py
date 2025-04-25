from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from keyboards.reply import major_keyboard, grade_keyboard, province_keyboard, get_cities_keyboard
from db import add_or_update_user, is_username_taken
from keyboards.reply import main_menu_keyboard

router = Router()

# وضعیت‌ها
class Register(StatesGroup):
    major = State()
    grade = State()
    province = State()
    city = State()
    username = State()

# شروع ثبت‌نام
async def start_registration(message: Message, state: FSMContext):
    await message.answer("رشته تحصیلیتو انتخاب کن:", reply_markup=major_keyboard())
    await state.set_state(Register.major)

# رشته
@router.message(Register.major)
async def get_major(message: Message, state: FSMContext):
    await state.update_data(major=message.text)
    await message.answer("پایه تحصیلیتو انتخاب کن:", reply_markup=grade_keyboard())
    await state.set_state(Register.grade)

# پایه
@router.message(Register.grade)
async def get_grade(message: Message, state: FSMContext):
    await state.update_data(grade=message.text)
    await message.answer("استان محل تحصیلتو انتخاب کن:", reply_markup=province_keyboard())
    await state.set_state(Register.province)

# استان
@router.message(Register.province)
async def get_province(message: Message, state: FSMContext):
    province = message.text
    await state.update_data(province=province)
    await message.answer("حالا شهرتو انتخاب کن:", reply_markup=get_cities_keyboard(province))
    await state.set_state(Register.city)

# شهر
@router.message(Register.city)
async def get_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    await message.answer("یه یوزرنیم برای خودت وارد کن (فقط حروف و عدد، بدون فاصله و فارسی):", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Register.username)

# یوزرنیم
@router.message(Register.username)
async def get_username(message: Message, state: FSMContext):
    username = message.text.strip()

    if not username.isascii() or " " in username or is_username_taken(username):
        await message.answer("یوزرنیم معتبر نیست یا قبلاً ثبت شده. لطفاً یه یوزرنیم دیگه وارد کن:")
        return

    await state.update_data(username=username)

    data = await state.get_data()
    add_or_update_user(
        message.from_user.id,
        username,
        data["grade"],
        data["major"],
        data["province"],
        data["city"]
    )

    await message.answer("پروفایلت با موفقیت ساخته شد و ۵ سکه هدیه گرفتی! {0}".format(chr(0x1F381)))
    await message.answer("از منوی زیر استفاده کن:", reply_markup=main_menu_keyboard())

    await state.clear()
