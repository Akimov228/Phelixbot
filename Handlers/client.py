from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
from Keyboards.client_kb import start_markup


# @dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=f"Салам хозяин {message.from_user.first_name}",
                           reply_markup=start_markup)
    # await message.answer("This is an answer method")
    # await message.reply("This is a reply method")


async def info_handler(message: types.Message):
    await message.reply("Сам разбирайся!")


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 1", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Президент КР в данное время"
    answers = [
        'Жапаров',
        'Путин',
        'Обама',
        'Атамбаев',
        'Сооронбаев',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Жапаров",
        # open_period=5,
        reply_markup=markup
    )




async def send_mem(message: types.Message):


    photo = open("Media/mem.jpg", "rb")
    await bot.send_photo(chat_id=message.chat.id, photo=photo)

@dp.message_handler(commands=['pin'],commands_prefix='/!')
async def pin_message(message: types.Message):
    # if message.text.startswith('!'):
    await bot.pin_chat_message(message.chat.id, message.message_id)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(send_mem, commands=['meme'])
    # dp.register_message_handler(pin_message, commands=['pin'])
