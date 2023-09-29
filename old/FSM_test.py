import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, F, html
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardRemove,\
      InlineKeyboardButton, KeyboardButton, WebAppInfo, CallbackQuery, ReplyKeyboardMarkup
from aiogram.utils.markdown import hbold
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from config import TOKEN
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from sqlite3_get import records, sql_get_currency
# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

my_router = Router(name=__name__)
dp.include_router(my_router)


# SERVICE SECTION
def format_number_with_spaces(number):
    # Преобразуем число в строку и разделяем его разряды пробелами
    formatted_number = "{: ,}".format(number)
    return formatted_number

# FSM
class Form(StatesGroup):
    currency = State()
    amount = State()


@my_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.currency)
    await message.answer(
        "Из какой валюты будет обмен?",
        reply_markup=inline_from_db.as_markup(),
    )

@my_router.callback_query(Form.currency)
async def process_currency(callback_query: CallbackQuery, state: FSMContext) -> None:
    await state.update_data(currency=callback_query.data)
    await state.set_state(Form.amount)
    await callback_query.message.answer(f"ТЫ ВЫБРАЛ {callback_query.data}")
    await callback_query.message.answer("ТЕПЕРЬ ВВЕДИ СУММУ:")



@my_router.message(Form.amount, lambda message: not message.text.isdigit())
async def wrong_amount(message: Message, state: FSMContext) -> None:
    await message.reply("Здесь должно быть число! Давай ещё раз!")


@my_router.message(Form.amount)
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


@my_router.message(Command('kb'))
async def message_handler5(message: Message):
    await message.answer('Reply keyboard shown', reply_markup=builder.as_markup())

@my_router.message(F.text == 'remove buttons')
async def message_handler6(message: Message):
    await message.answer('Button1 pushed', reply_markup=ReplyKeyboardRemove())

@my_router.message(F.text == 'inline buttons')
async def message_handler7(message: Message):
    await message.answer('Button1 pushed', reply_markup=builder_inline.as_markup())

@my_router.message(F.text.lower().contains('calc'))
async def message_handler_calc(message: Message):
    # await message.answer('Выбери исходную валюту:', reply_markup=inline_calc.as_markup())
    await message.answer('Выбери исходную валюту:', reply_markup=inline_from_db.as_markup())






# KEYBOARDS

builder = ReplyKeyboardBuilder()
builder.button(text='remove buttons', callback_data='button pushed').adjust(1)
builder.button(text='inline buttons', callback_data='button pushed').adjust(1)
builder.button(text='Exchange Rate', callback_data='cb2').adjust(1)
builder.button(text='calc', callback_data='cb2').adjust(1)
# builder.adjust(1, 1, 1)

# KEYBOARD INLINE TEST

builder_inline = InlineKeyboardBuilder()
builder_inline.button(text='Inline Button1', callback_data='cb1')
builder_inline.button(text='Inline Button2', callback_data='cb2')
builder_inline.button(text='Inline test filter', callback_data='f1')

url_button = InlineKeyboardButton(text='LINK!', url='https://ya.ru')
webapp_button = InlineKeyboardButton(text='WEBAPP!', web_app=WebAppInfo(url='https://taplink.cc/vnd'))

builder_inline.add(url_button, webapp_button)


# inline_from_db
inline_from_db = InlineKeyboardBuilder()
for num in records[1:]:
    inline_from_db.button(text=num[1], callback_data=num[1])






async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())