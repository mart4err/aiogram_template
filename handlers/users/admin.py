from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from loader import db
from keyboards.inline import buttons as INLINE_KB
from states.admin import AdminState as STATE

router = Router()

@router.message(Command('test'))
async def test(message: types.Message, state: FSMContext):
	await state.set_state(STATE.are_you_sure)
	await message.answer('Вы уверены что хотите протестировать? :)', reply_markup=INLINE_KB.you_sure_markup)

@router.callback_query(STATE.are_you_sure)
async def you_sure_markup(callback: types.CallbackQuery, state: FSMContext):
  	await state.clear()
  	await callback.message.answer(f'Вы выбрали {callback.data}')
  	await callback.answer()