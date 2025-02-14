from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


you_sure_markup = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="✅ Да", callback_data='yes'),
    InlineKeyboardButton(text="❌ Нет", callback_data='no')
]])