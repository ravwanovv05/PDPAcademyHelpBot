from aiogram import types
from aiogram.utils.markdown import bold
from bot.api.users import user_without_user_role


def escape_markdown(text: str) -> str:
    if text is None:
        return ""
    escape_chars = r'\_*[]()~`>#+-=|{}.!'
    return ''.join(f'\\{char}' if char in escape_chars else char for char in text)


async def staffs_handler(message: types.Message):
    staffs = user_without_user_role()
    managers = bold('Managers\n')
    admins = bold('\nAdmins\n')

    for staff in staffs:
        first_name = escape_markdown(staff.get('first_name'))
        last_name = escape_markdown(staff.get('last_name'))

        if staff.get('role') == 'manager':
            managers += f"{first_name} {last_name}\n"
        else:
            admins += f"{first_name} {last_name}\n"

    text = managers + admins

    await message.answer(text, parse_mode='MarkdownV2')
