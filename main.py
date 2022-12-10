from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging
TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)





@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Здорова {message.from_user.username}-----')


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 1", callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Самая большая страна"
    answers = [
        'Канада',
        'Китай',
        'США',
        'Россия',
        'Монголия',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Россия ",
        open_period=59,
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):

    question = "Кто первый президент США?"
    answers = [
        "Клинтон",
        "Вашингтон",
        "Буш",
        "Кеннеди",
        "Путин",
        "Обама",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Первый президент Америки - Джордж Вашингтон",
        open_period=59,
    )


@dp.message_handler(commands=['meme'])
async def send_mem(message: types.Message):


    photo = open("Media/mem.jpg", "rb")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler()
async def echo(message: types.Message):
    print(message)
    if message.text.isnumeric():
        await bot.send_message(message.from_user.id, int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)

if __name__ == '__main__' :
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
