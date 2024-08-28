from aiogram import types
from dotenv import load_dotenv
from bot.api.users import create_user
from bot.buttons.reply_buttons.main import main_buttons
from bot.utils.users import read_file, write_file

load_dotenv()


async def start_handler(message: types.Message):

    if not str(message.chat.id).startswith('-'):
        telegram_id = message.from_user.id
        users = read_file('users.json')
        users_id = []

        for user in users:
            users_id.append(user['telegram_id'])

        if telegram_id not in users_id:
            users.append(
                {
                    "telegram_id": telegram_id,
                }
            )
            write_file('users.json', users)
            create_user(
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                username=message.from_user.username,
                telegram_id=telegram_id,
            )
        text = 'Assalomu Aleykum, xush kelibsiz, nima kerak bo\'lsa shu tugmani bosing 👇🏻'

        await message.answer(text, reply_markup=main_buttons())
