from aiogram import Bot, Dispatcher
from decouple import config




ADMINS = [1029680818,]
TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
