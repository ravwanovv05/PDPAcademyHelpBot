from aiogram import types, Bot
from bot.buttons.inline_buttons.solveproblems import in_process_button, done_button2


async def done_problems_handler(query: types.CallbackQuery, bot: Bot):
    telegram_ids = query.data.split('_')[-1]
    if telegram_ids == "None":
        await bot.edit_message_reply_markup(chat_id=query.message.chat.id, message_id=query.message.message_id, reply_markup=in_process_button(telegram_ids))
    else:
        telegram_ids = query.data.split('_')[-1].replace("'", '').replace('[', '').replace(']', '').replace(',', '').split()
        if str(query.from_user.id) in telegram_ids:
            await bot.edit_message_reply_markup(chat_id=query.message.chat.id, message_id=query.message.message_id, reply_markup=in_process_button(telegram_ids))


async def problem_solved_button_handler(query: types.CallbackQuery, bot: Bot):
    telegram_ids = query.data.split('_')[-1]
    if telegram_ids == "None":
        await bot.edit_message_reply_markup(chat_id=query.message.chat.id, message_id=query.message.message_id, reply_markup=done_button2())
    else:
        telegram_ids = query.data.split('_')[-1].replace("'", '').replace('[', '').replace(']', '').replace(',', '').split()
        if str(query.from_user.id) in telegram_ids:
            await bot.edit_message_reply_markup(chat_id=query.message.chat.id, message_id=query.message.message_id, reply_markup=done_button2())
