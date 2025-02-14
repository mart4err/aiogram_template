from aiogram import Router, types
from aiogram.filters import Command

from data.config import ADMINS

router = Router()


@router.message(Command('help'))
async def bot_help(message: types.Message):
    # Команды для всех пользователей
    text = ["Команды: ",
            "/start - Перезапуск бота",
            "/help - Список команд"]

    # Команды для администраторов
    if message.from_user.id in ADMINS:
        text.append("\n")
        text.append("Команды администратора: ")
        text.append("/test - Тестовая команда")

    await message.answer(text="\n".join(text))