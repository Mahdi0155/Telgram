from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# منوی اصلی
def main_menu_keyboard():
    buttons = [
        ["📊 محاسبه درصد", "📚 نحوه مطالعه دروس"],
        ["❓ رفع اشکال", "💬 سوال مشاوره‌ای"],
        ["🪙 سکه رایگان", "🛍 خرید سکه / سکه نامحدود"],
        ["👤 پروفایل من"]
    ]
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=b) for b in row] for row in buttons], resize_keyboard=True)

# رشته‌ها
def major_keyboard():
    buttons = ["تجربی", "ریاضی", "انسانی"]
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=b)] for b in buttons], resize_keyboard=True)

# پایه‌ها
def grade_keyboard():
    buttons = ["دهم", "یازدهم", "دوازدهم"]
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=b)] for b in buttons], resize_keyboard=True)

# استان‌ها
def province_keyboard():
    provinces = ["تهران", "فارس", "اصفهان", "خراسان رضوی", "آذربایجان شرقی"]
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=p)] for p in provinces], resize_keyboard=True)

# شهرها برای هر استان
def get_cities_keyboard(province: str):
    cities_map = {
        "تهران": ["تهران", "اسلامشهر", "شهریار"],
        "فارس": ["شیراز", "مرودشت", "فیروزآباد"],
        "اصفهان": ["اصفهان", "کاشان", "نجف‌آباد"],
        "خراسان رضوی": ["مشهد", "نیشابور", "تربت‌حیدریه"],
        "آذربایجان شرقی": ["تبریز", "مراغه", "مرند"]
    }

    city_buttons = [KeyboardButton(text=city) for city in cities_map.get(province, ["نامشخص"])]
    return ReplyKeyboardMarkup(keyboard=[[btn] for btn in city_buttons], resize_keyboard=True)
