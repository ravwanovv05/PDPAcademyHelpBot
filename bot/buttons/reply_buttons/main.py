from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_buttons():
    keyboard_problem = KeyboardButton(text='Muammolar')

    builder = ReplyKeyboardBuilder()
    builder.add(keyboard_problem)

    return builder.as_markup(resize_keyboard=True)
