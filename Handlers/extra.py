from aiogram import types, Dispatcher
from config import bot, ADMINS
from random import choice



# DRY - Don't Repeat Yourself
# @dp.message_handler()
async def echo(message: types.Message):
    if message.chat.type != "private":
        bad_words = ['пошел', 'пошёл', 'дурак', 'чокун','иди']
        username = f"@{message.from_user.username}" \
            if message.from_user.username is not None else message.from_user.full_name

        for i in bad_words:
            if i in message.text.lower().replace(' ', ''):
                await bot.delete_message(message.chat.id, message.message_id)
                await message.answer(f"Не матерись {username}, "
                                     f"сам ты {i}!")

    if message.text.startswith('.'):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.text == 'game':
        if message.from_user.id  in ADMINS:
            games = ['🎲','🎯','🎳','🎰','⚽','️🏀']
            emoji = choice(games)
            a = await bot.send_dice(message.chat.id, emoji=emoji)
            # print(a.dice.value)


def register_handler_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
