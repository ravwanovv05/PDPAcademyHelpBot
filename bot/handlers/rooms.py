from aiogram import types, Bot
from aiogram.fsm.context import FSMContext
from bot.buttons.inline_buttons.rooms import rooms_list_buttons
from bot.buttons.inline_buttons.things import things_buttons
from bot.models.things import Thing


async def request_room_number_handler(message: types.Message, state: FSMContext):
    await state.set_state(Thing.room)
    await message.answer('Iltimos xona raqamini tanlang', reply_markup=rooms_list_buttons())


async def get_room_number_handler(query: types.CallbackQuery, state: FSMContext, bot: Bot):
    if query.data.startswith('nextroom'):
        page = int(query.data.split('_')[-1]) + 1

        await state.set_state(Thing.room)
        await bot.edit_message_reply_markup(
            chat_id=query.message.chat.id, message_id=query.message.message_id,
            reply_markup=rooms_list_buttons(page)
        )
    elif query.data.startswith('prevroom'):
        page = int(query.data.split('_')[-1]) - 1

        await state.set_state(Thing.room)
        await bot.edit_message_reply_markup(
            chat_id=query.message.chat.id, message_id=query.message.message_id,
            reply_markup=rooms_list_buttons(page)
        )
    else:
        await bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id)
        await state.update_data(room=f"{query.data.split('_')[0]} {query.data.split('_')[1]}")
        await state.set_state(Thing.things)
        await bot.send_message(chat_id=query.message.chat.id, text='Kerakli narsani tanlang.', reply_markup=things_buttons())

