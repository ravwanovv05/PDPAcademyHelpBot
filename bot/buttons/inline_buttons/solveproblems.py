from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def done_button1(telegram_id=None):
    button1 = InlineKeyboardButton(text='Bajarish', callback_data=f"do_it_{telegram_id}")

    builder = InlineKeyboardBuilder()
    builder.add(button1)

    return builder.as_markup()


def in_process_button(telegram_id=None):
    print(telegram_id)
    button1 = InlineKeyboardButton(text='Jarayonda...', callback_data=f"in_process_{telegram_id}")

    builder = InlineKeyboardBuilder()
    builder.add(button1)

    return builder.as_markup()


def done_button2():
    button1 = InlineKeyboardButton(text='Bajarildi', callback_data='done')

    builder = InlineKeyboardBuilder()
    builder.add(button1)

    return builder.as_markup()

