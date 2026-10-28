from aiogram.utils.keyboard import InlineKeyboardBuilder


def inline_choose_gender() ->InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(text="🙍‍♂️", callback_data="gender:man")
    builder.button(text="🙍‍♀️", callback_data="gender:woman")
    return builder