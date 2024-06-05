from aiogram.fsm.state import StatesGroup, State

class CoinStep(StatesGroup):
    upper_threshold = State()
    lower_threshold = State()
    accept = State()