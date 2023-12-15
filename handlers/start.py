from aiogram import Router
from aiogram import types
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer('Hello this is a bot to download music from spotify!\n'
                         'If you have access to this bot just send me link to song and I download it.')