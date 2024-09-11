import os
from aiogram import types, Bot
from aiogram.fsm.context import FSMContext

from bot.api.users import user_detail
from bot.buttons.inline_buttons.solveproblems import done_button1
from bot.models.things import Thing


async def thing_handler(query: types.CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()

    if query.data == 'done':
        text = f"Xona: {data['room']}\nKerakli narsalar: "
        things = list(set(data['things']['things']))
        responsible_users = list(data['things']['responsible_users'])

        for thing in things:
            if things[-1] != thing:
                text += thing + ', '
            else:
                text += thing
        telegram_ids = []
        for responsible_user in responsible_users:
            text += ' \n' + f"[{responsible_user['first_name']}](tg://user?id={responsible_user['telegram_id']})"
            telegram_ids.append(responsible_user['telegram_id'])

        group_id = os.getenv('GROUP_ID')

        await state.clear()
        await query.message.delete()
        await bot.send_message(group_id, text, reply_markup=done_button1(telegram_ids), parse_mode='Markdown')
        await bot.send_message(query.from_user.id, 'Muammolar tez orada bartaraf etiladi!')
    elif query.data == 'another':
        await state.set_state(Thing.another)
        await bot.delete_message(query.message.chat.id, query.message.message_id)
        await bot.send_message(query.message.chat.id, 'Muammoni yozib qoldiring.')
    else:
        try:
            data['things']['things'].append(query.data.split('_')[0])
            if query.data.split('_')[1] not in data['things']['telegram_ids']:
                data['things']['responsible_users'].append(
                    {
                        'first_name': user_detail(int(query.data.split('_')[-1]))['first_name'],
                        'telegram_id': query.data.split('_')[1]
                    }
                )
                data['things']['telegram_ids'].append(query.data.split('_')[1])
            await state.update_data(things=data['things'])
        except:
            await state.update_data(
                things={
                    'things': [query.data.split('_')[0]],
                    'responsible_users': [
                        {
                            'first_name': user_detail(int(query.data.split('_')[-1]))['first_name'],
                            'telegram_id': query.data.split('_')[1],
                         }
                    ],
                    'telegram_ids': [query.data.split('_')[1]]
                }
            )


async def another_handler(message: types.Message, bot: Bot, state: FSMContext):
    await state.update_data(another=message.text)
    data = await state.get_data()
    text = f"Xona: {data['room']}\nMuammo: {data['another']}"
    group_id = os.getenv('GROUP_ID')

    await state.clear()
    await message.answer('Muammolar tez orada bartaraf etiladi.')
    await bot.send_message(group_id, text, reply_markup=done_button1())
