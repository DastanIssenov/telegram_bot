from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import logging

import app.keyboard as kb

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(f"""Мен сізге қалай көмектесе алатынымды мәзірден таңдаңыз

Выберите из меню, чем я могу Вам помочь""")
    await message.answer(f"""Интерфейстің тілін таңдауыңызды сұраймыз

Просим Вас выбрать язык интерфейса""", 
                         reply_markup=kb.settings)

@router.callback_query(F.data == "lang_ru")
async def lang_ru(callback: Message):
    await callback.message.answer("Русский",
                                  reply_markup=kb.russian_menu)

@router.callback_query(F.data == "lang_kz")
async def lang_kz(callback: Message):
    await callback.message.answer("Қазақша",
                                    reply_markup=kb.russian_menu)


# @router.message(F.text)
# async def find_suitable_answer(message: Message):
#     await )
