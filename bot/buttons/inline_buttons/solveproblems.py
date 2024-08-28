from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def done_button1():
    button1 = InlineKeyboardButton(text='Bajarish', callback_data='do_it')

    builder = InlineKeyboardBuilder()
    builder.add(button1)

    return builder.as_markup()


def in_process_button():
    button1 = InlineKeyboardButton(text='Jarayonda...', callback_data='in_process')

    builder = InlineKeyboardBuilder()
    builder.add(button1)

    return builder.as_markup()


def done_button2():
    button1 = InlineKeyboardButton(text='Bajarildi', callback_data='done')

    builder = InlineKeyboardBuilder()
    builder.add(button1)

    return builder.as_markup()

