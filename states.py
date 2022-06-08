from aiogram.dispatcher.filters.state import StatesGroup, State

class botStates(StatesGroup):
    STATE_NOW = State()
    STATE_TODAY = State()
    STATE_TOMORROW = State()
    STATE_FIVE_DAYS = State()
    STATE_SETTINGS = State()