from aiogram import Router, types
from aiogram.filters import CommandStart

# from loader import db Для использования базы данных


router = Router()

@router.message(CommandStart())
async def do_start(message: types.Message):
	await message.answer('Hello World!')

	# db.add_user(telegram_id=message.from_user.id) Метод в utils/db/mysql/mysql.py для добавления пользователя в базу данных если его там нет