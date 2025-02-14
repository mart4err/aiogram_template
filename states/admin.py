from aiogram.filters.state import StatesGroup, State

class AdminState(StatesGroup):
    are_you_sure = State()