from aiogram import F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, WebAppInfo, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from create_bot import my_router
from sqlite3_get import print_rate
from keyboards import *
from logger import *


@my_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    webappbutton = KeyboardButton(text='WEBAPP BUTTON', web_app=WebAppInfo(url="https://taplink.cc/vnd"))
    builder2 = ReplyKeyboardBuilder()
    builder2.add(webappbutton)
    await message.answer(f"Hello, {message.from_user.full_name}!", reply_markup=builder2.as_markup())
    await message.delete()
    logger.info("command Start pressed")

@my_router.message(Command('kb'))
async def message_handler_command_kb(message: Message):
    await message.answer('.' ,reply_markup=builder.as_markup())
    await message.delete()
    logger.info("command kb pressed")

@my_router.callback_query(F.data == 'pic')
async def callback_query_picture(call):
    await call.message.answer_photo("https://downloader.disk.yandex.ru/preview/3ce8fff9f2add0fcf7ba82db827102b192c678d508a1387d1c791411abbb139e/650bffc8/C_xgAb0IJNQ971p-5C0cD5mX8CU52JCffu0wkN40qmllbQHW_MwBRBzdNRQ3XbAGCiiD7XBDS8rfAng6QImYyQ%3D%3D?uid=0&filename=photo_2023-09-18%2016.00.30.jpeg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")
    await call.message.delete()
    logger.info("command pic pressed")

@my_router.message(F.text == 'inline buttons')
async def message_handler_inline_kb(message: Message):
    await message.answer('choose', reply_markup=builder_inline.as_markup())
    await message.delete()
    logger.info("command inline pressed")

@my_router.message(F.text == 'Exchange Rate')
async def message_get_rate(message: Message):
    await message.answer(print_rate())
    await message.delete()
    logger.info(f"command exchange pressed")

@my_router.message(F.text == 'remove buttons')
async def message_remove_kb(message: Message):
    await message.answer('removed', reply_markup=ReplyKeyboardRemove())
    await message.delete()
    logger.info(f"command remove kb pressed")

@my_router.message(F.text.lower().contains('спасибо'))
async def message_handler_mersi(message: Message):
    # await message.answer_animation('CgACAgQAAxkBAAIC9GUEaho8UstXBCHQlhiJCC9DmzBGAAKLAAM_lQRQoW5y7xikiDUwBA')
    await message.reply_animation('CgACAgQAAxkBAAIC9GUEaho8UstXBCHQlhiJCC9DmzBGAAKLAAM_lQRQoW5y7xikiDUwBA')
    logger.info(f"command thanx pressed")