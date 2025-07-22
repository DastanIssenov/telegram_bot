from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder 

russian_menu = ReplyKeyboardMarkup(keyboard = [
    [
        KeyboardButton(text="💳 Покупка и возврат билетов")
    ],
    [
        KeyboardButton(text="📕 Льготы и правила проезда")
    ],
    [
        KeyboardButton(text="🫶 Промоакции")
    ],
    [
        KeyboardButton(text="📋 Оставить обращение")
    ],
    [
        KeyboardButton(text="🔍 Проверка статуса заявки")
    ],
    [
        KeyboardButton(text="🌐 Сменить язык")
    ]

],one_time_keyboard = True)

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "Русский", callback_data= "lang_ru")],
    [InlineKeyboardButton(text = "Қазақша", callback_data= "lang_kz")]
    ]
)

async def inline_cars():
    keyboard = ReplyKeyboardBuilder()

    for car in ["Русский", "Қазақша"]:
        keyboard.add(KeyboardButton(text=car))
    return keyboard.adjust(2).as_markup()