from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import logging

import app.keyboard as kb

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(f"""Hello, I am your bot!
                         {message.from_user.id}
                         {message.from_user.first_name}""", 
                         reply_markup=await kb.inline_cars())

@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer("This is a help message. How can I assist you?")

@router.message(F.text == "Как дела?")
async def how_are_you(message: Message):
    await message.answer("OK")

@router.message(F.photo)
async def photo_handler(message: Message):
    logging.info(f"Photo received in chat {message.chat.id}")
    await message.answer_photo(
        photo=message.photo[-1].file_id,
        caption="Look at this fool ahahahaha"
    )
