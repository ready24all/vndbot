from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from create_bot import my_router
from datetime import datetime
# from keyboards import *
from config import DB_CONFIG
# import sqlite3
import mysql.connector
from logger import logger

# FSM
class Adminrate(StatesGroup):
    rate_admin = State()



@my_router.message(Command('rate'))
async def message_handler_rate(message: Message, state: FSMContext):
    await message.delete()
    await state.set_state(Adminrate.rate_admin)
    await message.answer(
        "Введите курс в формате \"USDT USD RUB\", например:\n23900 23900 241"
    )

@my_router.message(Adminrate.rate_admin)
async def message_handler_rate2(message: Message, state: FSMContext) -> None:
    await state.update_data(rate_adm=message.text)
    await state.clear()
    rate_list = [datetime.now().strftime("%Y-%m-%d"), *message.text.split(), datetime.now()]
    insert_rate(rate_list)
    logger.info('rate added')
    await message.delete()
    await message.answer("Курс успешно добавлен")


def insert_rate(rate_list):
    with mysql.connector.connect(**DB_CONFIG) as db_connection:
        with db_connection.cursor() as cursor:
            sql_request = "INSERT INTO DAY_RATE (DATE, USDT, USD, RUB, TIMESTAMP) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql_request, rate_list)
        db_connection.commit()






