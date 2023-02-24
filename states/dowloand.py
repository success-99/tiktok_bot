from aiogram.dispatcher.filters.state import StatesGroup, State
class Dow(StatesGroup):
    input = State()
    output = State()
    text = State()
# 
