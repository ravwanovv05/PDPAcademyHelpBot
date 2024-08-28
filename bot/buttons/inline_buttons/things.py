from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.api.things import things_list
from bot.api.users import user_detail


def things_buttons():
    things = things_list()
    builder = InlineKeyboardBuilder()

    c = 0
    for thing in things:
        user = user_detail(int(thing['responsible_user']))
        button = InlineKeyboardButton(
            text=thing['name'], callback_data=f"{thing['name']}_{user['telegram_id']}_{user['first_name']}"
        )

        c += 1
        if c != 1 and c % 2 != 0:
            builder.row(button)
        else:
            builder.add(button)

    done_button = InlineKeyboardButton(text='Tasdiqlash ✅', callback_data='done')
    another_button = InlineKeyboardButton(text='Boshqalar', callback_data='another')
    builder.row(another_button, done_button)

    return builder.as_markup()
