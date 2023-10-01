from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from create_bot import my_router
from datetime import datetime
from keyboards import *
from config import DB_NAME
import sqlite3
import logger

# FSM
class Adminrate(StatesGroup):
    rate_admin = State()



@my_router.message(Command('rate'))
async def message_handler_rate(message: Message, state: FSMContext):
    await state.set_state(Adminrate.rate_admin)
    await message.answer(
        "Введите курс в формате \"USDT USD RUB\", например:\n23900 23900 241"
    )

# @my_router.message(Adminrate.rate_admin)
# async def message_handler_rate2(message: Message, state: FSMContext) -> None:
#     await state.update_data(rate_adm=message.text)
#     await state.clear()
#     rate_list = [datetime.now().strftime("%Y-%m-%d"), *message.text.split(), datetime.now()]
#     with sqlite3.connect(DB_NAME) as sql_conn:
#         sql_request = "INSERT INTO DAY_RATE VALUES(?, ?, ?, ?, ?)"
#         sql_conn.execute(sql_request, rate_list)
#         sql_conn.commit()
#     await message.answer("Курс успешно добавлен")

@my_router.message(Adminrate.rate_admin)
async def message_handler_rate2(message: Message, state: FSMContext) -> None:
    await state.update_data(rate_adm=message.text)
    await state.clear()
    rate_list = [datetime.now().strftime("%Y-%m-%d"), *message.text.split(), datetime.now()]
    insert_rate(rate_list)
    logger.debug('rate added')
    await message.answer("Курс успешно добавлен")



def insert_rate(rate_list):
    with sqlite3.connect(DB_NAME) as sql_conn:
        sql_request = "INSERT INTO DAY_RATE VALUES(?, ?, ?, ?, ?)"
        sql_conn.execute(sql_request, rate_list)
        sql_conn.commit()



# with sqlite3.connect(DB_NAME) as sql_conn:
#     sql_request = "INSERT INTO DAY_RATE VALUES(?, ?, ?, ?)"
#     sql_conn.execute(sql_request, ('1991-12-22', 1, 1, 1))
#     sql_conn.commit()