from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
ADMINS = [1029680818,]
TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
