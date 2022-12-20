from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from Keyboards import client_kb


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    age = State()
    region = State()
    direction = State()
    group = State()
    submit = (State)


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.id.set()
        await message.answer("назови свой id", reply_markup=client_kb.cancel_markup)
    else:
        await message.answer("Пиши в личке!")


async def load_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.text
    await FSMAdmin.next()
    await message.answer("Как звать?", reply_markup=client_kb.cancel_markup)


async def load_name(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.answer("Сколько лет?", reply_markup=client_kb.cancel_markup)


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа")
    elif int(message.text) < 5 or int(message.text) > 50:
        await message.answer("Возростное ограничение!")
    else:
        async with state.proxy() as data:
            data['age'] = int(message.text)
        await FSMAdmin.next()
        await message.answer("Откуда будешь?", reply_markup=client_kb.cancel_markup)


async def load_region(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['region'] = message.text
        await FSMAdmin.next()
        await message.answer("Выбери направление??", reply_markup=client_kb.cancel_markup)


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer("Группа?)", reply_markup=client_kb.cancel_markup)


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await message.answer(f"Твой ID: {data['id']}\nИмя: {data['name']}\nВозраст: {data['age']} "
                             f"\nРегион: {data['region']}\nНаправление: {data['direction']}\nГруппа: {data['group']}")
    await FSMAdmin.next()
    await message.answer("Все верно?", reply_markup=client_kb.submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        # Запись в БД
        await state.finish()
        await message.answer("Отлично,ты записан!")
    elif message.text.lower() == "нет":
        await state.finish()
        await message.answer("Ну и пошел ты!")
    else:
        await message.answer('НИПОНЯЛ!?')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Ну и пошел ты!")


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_fsm, Text(equals='cancel', ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_region, state=FSMAdmin.region)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)