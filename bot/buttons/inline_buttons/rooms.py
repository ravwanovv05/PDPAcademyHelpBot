from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.api.rooms import rooms_list


def rooms_list_buttons(page: int = 1):
    rooms = rooms_list()
    start_index = (page - 1) * 10
    end_index = min(start_index + 10, len(rooms))

    builder = InlineKeyboardBuilder()

    c = 0
    for i in range(start_index, end_index):
        button = InlineKeyboardButton(
            text=f"{rooms[i]['room_number']} xona",
            callback_data=f"{rooms[i]['name']}_{rooms[i]['room_number']}_{rooms[i]['id']}"
        )

        c += 1
        if c != 0 and c % 2 != 0:
            builder.row(button)
        else:
            builder.add(button)

    if page > 1 and end_index < len(rooms):
        builder.row(
            InlineKeyboardButton(
                text='🔙', callback_data=f"prevroom_{page}"
            ),
            InlineKeyboardButton(
                text='🔜', callback_data=f"nextroom_{page}"
            )
        )
        return builder.as_markup()

    if page > 1:
        builder.row(
            InlineKeyboardButton(
                text='🔙', callback_data=f"prevroom_{page}"
            )
        )
        return builder.as_markup()

    if end_index < len(rooms):
        builder.row(
            InlineKeyboardButton(
                text='🔜', callback_data=f"nextroom_{page}"
            )
        )
        return builder.as_markup()
