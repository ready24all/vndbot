import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardRemove,\
      InlineKeyboardButton, KeyboardButton, WebAppInfo, CallbackQuery
from aiogram.utils.markdown import hbold
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder, ReplyKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters.callback_data import CallbackData
from config import TOKEN
from sqlite3_get import records, sql_get_currency

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

my_router = Router(name=__name__)
dp.include_router(my_router)

# FSM
class Form(StatesGroup):
    currency = State()
    amount = State()



@my_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    webappbutton = KeyboardButton(text='WEBAPP BUTTON', web_app=WebAppInfo(url="https://taplink.cc/vnd"))
    await message.answer(
        reply_markup=ReplyKeyboardMarkup(
            keyboard=KeyboardButton(text='WEBAPP BUTTON', web_app=WebAppInfo(url="https://taplink.cc/vnd")),
            resize_keyboard=True,
        ),
    )





@my_router.message(Command('kb'))
async def message_handler5(message: Message):
    await message.answer('Reply keyboard shown', reply_markup=builder.as_markup())
    await message.delete()

@my_router.message(F.text == 'remove buttons')
async def message_handler6(message: Message):
    await message.answer('Button1 pushed', reply_markup=ReplyKeyboardRemove())
    await message.delete()

@my_router.message(F.text == 'inline buttons')
async def message_handler7(message: Message):
    await message.answer('Button1 pushed', reply_markup=builder_inline.as_markup())
    await message.delete()


@my_router.message(F.text.lower().contains('спасибо'))
async def message_handler_mersi(message: Message):
    # await message.answer_animation('CgACAgQAAxkBAAIC9GUEaho8UstXBCHQlhiJCC9DmzBGAAKLAAM_lQRQoW5y7xikiDUwBA')
    await message.reply_animation('CgACAgQAAxkBAAIC9GUEaho8UstXBCHQlhiJCC9DmzBGAAKLAAM_lQRQoW5y7xikiDUwBA')


@my_router.callback_query(F.data == 'f1')
async def callback_query_handler(call):
    await call.message.answer(call.data)
    await call.message.answer('TEST PICTURE SENDING')
    await call.message.answer_photo("https://aprioritravel.com/images/argentinu/Argentina_Houses_Roads_478950.jpg")
    await call.message.delete()




@my_router.message(F.text == 'Exchange Rate')
async def message_handler8(message: Message):
    await message.answer(rate)


@my_router.message(F.text.lower().contains('calc'))
async def message_handler_calc(message: Message, state: FSMContext):
    await state.set_state(Form.currency)
    await message.answer(
        "Из какой валюты будет обмен?",
        reply_markup=inline_from_db.as_markup(),
    )


@my_router.callback_query(Form.currency)
async def process_name(callback_query: CallbackQuery, state: FSMContext) -> None:
    await state.update_data(currency=callback_query.data)
    await state.set_state(Form.amount)
    await callback_query.message.answer(f"ТЫ ВЫБРАЛ {callback_query.data}")
    await callback_query.message.answer("ТЕПЕРЬ ВВЕДИ СУММУ:")

@my_router.message(Form.amount)
async def process_amount(message: CallbackQuery, state: FSMContext) -> None:
    await state.update_data(amount=message.text)
    data = await state.get_data()
    await state.clear()
    await message.answer(f"ТЫ ХОЧЕШЬ ПОМЕНЯТЬ {message.text} {data.get('currency')}")
    await message.answer("ЩА ПОСЧИТАЕМ...")
    rate = sql_get_currency(data.get('currency'))
    money = rate * int(data.get('amount'))
    print(data.get('amount'))
    await message.answer(f"Курс {rate} донгов за 1 {data.get('currency')}")
    await message.answer(f"К обмену будет {money} донгов")



# KEYBOARDS

builder = ReplyKeyboardBuilder()
builder.button(text='remove buttons', callback_data='button pushed').adjust(1)
builder.button(text='inline buttons', callback_data='button pushed').adjust(1)
builder.button(text='Exchange Rate', callback_data='cb2').adjust(1)
builder.button(text='calc', callback_data='cb2').adjust(1)
# builder.adjust(1, 1, 1)


builder_inline = InlineKeyboardBuilder()
builder_inline.button(text='Inline Button1', callback_data='f2')
builder_inline.button(text='Inline Button2', callback_data='f2')
builder_inline.button(text='Inline test filter', callback_data='f1')

url_button = InlineKeyboardButton(text='LINK!', url='https://ya.ru')
webapp_button = InlineKeyboardButton(text='WEBAPP!', web_app=WebAppInfo(url='https://taplink.cc/vnd'))

builder_inline.add(url_button, webapp_button)

# CALC keyboard
# inline_calc = InlineKeyboardBuilder()
# inline_calc.button(text='USDT', callback_data='usdt')
# inline_calc.button(text='USD', callback_data='usd')
# inline_calc.button(text='RUB', callback_data='rub')


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