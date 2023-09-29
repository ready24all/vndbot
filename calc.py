from aiogram.fsm.state import State, StatesGroup
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from create_bot import my_router
from sqlite3_get import sql_get_currency, records


# SERVICE SECTION
def format_number_with_spaces(number):
    # Преобразуем число в строку и разделяем его разряды пробелами
    formatted_number = "{: ,}".format(number)
    return formatted_number


# FSM
class Calc(StatesGroup):
    currency = State()
    amount = State()


@my_router.message(F.text == 'calc')
async def command_calc(message: Message, state: FSMContext) -> None:
    await state.set_state(Calc.currency)
    await message.answer(
        "Из какой валюты будет обмен?",
        reply_markup=inline_from_db.as_markup())

@my_router.callback_query(Calc.currency)
async def process_currency(callback_query: CallbackQuery, state: FSMContext) -> None:
    await state.update_data(currency=callback_query.data)
    await state.set_state(Calc.amount)
    await callback_query.message.answer(f"ТЫ ВЫБРАЛ {callback_query.data}")
    await callback_query.message.answer("ТЕПЕРЬ ВВЕДИ СУММУ:")



@my_router.message(Calc.amount, lambda message: not message.text.isdigit())
async def wrong_amount(message: Message, state: FSMContext) -> None:
    await message.reply("Здесь должно быть число! Давай ещё раз!")


@my_router.message(Calc.amount)
async def process_amount(message: Message, state: FSMContext) -> None:
    await state.update_data(amount=message.text)
    data = await state.get_data()
    await state.clear()
    await message.answer(f"ТЫ ХОЧЕШЬ ПОМЕНЯТЬ {message.text} {data.get('currency')}")
    await message.answer("ЩА ПОСЧИТАЕМ...")
    rate = sql_get_currency(data.get('currency'))
    money = rate * int(data.get('amount'))
    print(data.get('amount'))
    await message.answer(f"Курс {rate} донгов за 1 {data.get('currency')}")
    print(format_number_with_spaces(money))
    await message.answer(f"К обмену будет {format_number_with_spaces(money)} донгов")


# KEYBOARD FOR calc.py
inline_from_db = InlineKeyboardBuilder()
for num in records[1:4]:
    inline_from_db.button(text=num[1], callback_data=num[1])