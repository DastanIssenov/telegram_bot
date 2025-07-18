from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder 

main = ReplyKeyboardMarkup(keyboard = [
    [
        KeyboardButton(text="Кнопка 1"),
        KeyboardButton(text="Кнопка 2"),
        KeyboardButton(text="Кнопка 3")
    ],
    [
        KeyboardButton(text="Кнопка 4"),
        KeyboardButton(text="Кнопка 5")
    ]
],one_time_keyboard = True)

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "Youtube",
    url = "https://www.youtube.com/watch?v=qRyshRUA0xM&list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM&index=4")],
    [InlineKeyboardButton(text = "Google",
    url = "https://www.youtube.com/watch?v=qRyshRUA0xM&list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM&index=4")]
    ]
)

async def inline_cars():
    keyboard = ReplyKeyboardBuilder()

    for car in ["BMW", "Mercedes", "Audi", "Lada"]:
        keyboard.add(KeyboardButton(text=car))
    return keyboard.adjust(2).as_markup()