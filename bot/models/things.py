from aiogram.fsm.state import State, StatesGroup


class Thing(StatesGroup):
    room = State()
    things = State()
    another = State()
