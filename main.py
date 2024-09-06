import os
import sys
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from bot.handlers.rooms import request_room_number_handler, get_room_number_handler
from bot.handlers.things import thing_handler, another_handler
from bot.handlers.users import staffs_handler
from bot.models.things import Thing
from bot.handlers.main import start_handler
from bot.handlers.solveproblems import done_problems_handler, problem_solved_button_handler

load_dotenv()


token = os.getenv('BOT_TOKEN')


async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    bot = Bot(token)
    dp = Dispatcher()

    dp.message.register(start_handler, Command(commands='start'))
    dp.message.register(staffs_handler, Command(commands='staffs'))
    dp.message.register(request_room_number_handler, lambda message: message.text == 'Muammolar')
    dp.message.register(another_handler, Thing.another)
    dp.callback_query.register(get_room_number_handler, Thing.room)
    dp.callback_query.register(thing_handler, Thing.things)
    dp.callback_query.register(done_problems_handler, lambda query: query.data == 'do_it')
    dp.callback_query.register(problem_solved_button_handler, lambda query: query.data == 'in_process')

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
