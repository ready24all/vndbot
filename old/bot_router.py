import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, Filter
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery,\
      InlineKeyboardButton, KeyboardButton, WebAppInfo
from aiogram.utils.markdown import hbold
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder, ReplyKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from config import TOKEN

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

my_router = Router(name=__name__)
dp.include_router(my_router)

class MyCallback(CallbackData, prefix="my"):
    filter_mark: str

cb1 = MyCallback(filter_mark='p1').pack()
cb2 = MyCallback(filter_mark='p2').pack()
filter_p2 = MyCallback.filter(F.filter_mark == 'p2')

# Callback with Dispatcher
# @dp.callback_query(MyCallback.filter(F.filter_mark == 'p1'))
# async def process_callback_button(callback_query: CallbackQuery):
#     await callback_query.answer("CALL BACK with dp")
#     await callback_query.message.answer("CALL BACK with dp")

# Get animation ID
# @my_router.message(F.content_type.in_({'animation'}))
# async def message_handler3(message: Message):
#     await message.answer('Animation was getted')
#     await message.answer_animation(message.animation.file_id)
#     print(message.animation.file_id)

@my_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    webappbutton = KeyboardButton(text='WEBAPP BUTTON', web_app=WebAppInfo(url="https://taplink.cc/vnd"))
    builder2 = ReplyKeyboardBuilder()
    builder2.add(webappbutton)
    builder2.adjust(1)
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", reply_markup=builder2.as_markup())

# button1 = KeyboardButton('OPPPPPPP', web_app=WebAppInfo(url='https://taplink.cc/djsokol'))

@my_router.callback_query(MyCallback.filter(F.filter_mark == 'p1'))
async def process_callback_button1(callback_query: CallbackQuery):
    await callback_query.answer("CALL BACK with router", show_alert=True) 
    await callback_query.message.answer("CALL BACK with router answer")
    # await callback_query.answer(show_alert=True)

@my_router.message(F.text.lower().contains('спасибо'))
async def message_handler_mersi(message: Message):
    # await message.answer_animation('CgACAgQAAxkBAAIC9GUEaho8UstXBCHQlhiJCC9DmzBGAAKLAAM_lQRQoW5y7xikiDUwBA')
    await message.reply_animation('CgACAgQAAxkBAAIC9GUEaho8UstXBCHQlhiJCC9DmzBGAAKLAAM_lQRQoW5y7xikiDUwBA')


@my_router.message(F.text.lower().contains('обмен'))
async def message_handler1(message: Message):
    await message.answer('Contains обмен')

@my_router.message(F.text.lower().in_({'обмен', 'обменять'}))
async def message_handler2(message: Message):
    await message.answer('Ok! You want to change money, right???!!!!')

@my_router.message(F.text.lower() == 'kill')
async def message_handler3(message: Message):
    await message.answer('kill from my router!')

@my_router.message(F.text == '/kill')
async def message_handler4(message: Message):
    await message.answer('KILL command')

@my_router.message(Command('kb'))
async def message_handler5(message: Message):
    await message.answer('Reply keyboard shown', reply_markup=builder.as_markup())

@my_router.message(F.text.regexp(r"^(\d+)$").as_("digits"))
async def any_digits_handler(message: Message):
    await message.answer('Hello from my digits')

@my_router.message(F.text == 'remove buttons')
async def message_handler6(message: Message):
    await message.answer('Button1 pushed', reply_markup=ReplyKeyboardRemove())

@my_router.message(F.text == 'inline buttons')
async def message_handler7(message: Message):
    await message.answer('Button1 pushed', reply_markup=builder_inline.as_markup())


# @my_router.message(F.text == 'Exchange Rate')
# async def message_handler8(message: Message):
#     await message.answer(rate)

# @my_router.callback_query(MyCallback.filter(F.filter_mark == 'p2'))
@my_router.callback_query(filter_p2)
async def callback_query_handler(call):
    await call.message.answer(call.data)
    await call.message.answer('TEST PICTURE SENDING')
    await call.message.answer_photo("https://aprioritravel.com/images/argentinu/Argentina_Houses_Roads_478950.jpg")

@my_router.callback_query(F.data == 'f1')
async def callback_query_handler(call):
    await call.message.answer(call.data)
    await call.message.answer('f1 data test')

@my_router.message(F.text.lower().contains('calc'))
async def message_handler_calc(message: Message):
    await message.answer('Выбери исходную валюту:', reply_markup=inline_calc.as_markup())
    



# KEYBOARDS

builder = ReplyKeyboardBuilder()
builder.button(text='remove buttons', callback_data='button pushed').adjust(1)
builder.button(text='inline buttons', callback_data='button pushed').adjust(1)
builder.button(text='Exchange Rate', callback_data=cb2).adjust(1)
builder.button(text='calc', callback_data=cb2).adjust(1)
# builder.adjust(1, 1, 1)


builder_inline = InlineKeyboardBuilder()
builder_inline.button(text='Inline Button1', callback_data=cb1)
builder_inline.button(text='Inline Button2', callback_data=cb2)
builder_inline.button(text='Inline test filter', callback_data='f1')

url_button = InlineKeyboardButton(text='LINK!', url='https://ya.ru')
webapp_button = InlineKeyboardButton(text='WEBAPP!', web_app=WebAppInfo(url='https://taplink.cc/vnd'))

builder_inline.add(url_button, webapp_button)

# CALC keyboard
inline_calc = InlineKeyboardBuilder()
inline_calc.button(text='USDT', callback_data='usdt')
inline_calc.button(text='USD', callback_data='usd')
inline_calc.button(text='RUB', callback_data='rub')



async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())