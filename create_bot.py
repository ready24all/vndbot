from aiogram import Dispatcher, Router, Bot
from config import TOKEN

dp = Dispatcher()
my_router = Router(name=__name__)
bot = Bot(TOKEN)
dp.include_router(my_router)

