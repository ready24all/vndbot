from aiogram import Dispatcher, Router, Bot
from config import TOKEN
# import MySQL_create

dp = Dispatcher()
my_router = Router(name=__name__)
bot = Bot(TOKEN)
dp.include_router(my_router)

