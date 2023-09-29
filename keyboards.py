from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardButton, WebAppInfo



builder = ReplyKeyboardBuilder()
builder.button(text='remove buttons', callback_data='remove buttons').adjust(1)
builder.button(text='inline buttons', callback_data='inline buttons').adjust(1)
builder.button(text='Exchange Rate', callback_data='Exchange Rate').adjust(1)
builder.button(text='calc', callback_data='calc').adjust(1)


builder_inline = InlineKeyboardBuilder()
builder_inline.button(text='Pic', callback_data='pic')
url_button = InlineKeyboardButton(text='LINK!', url='https://ya.ru')
webapp_button = InlineKeyboardButton(text='WEBAPP!', web_app=WebAppInfo(url='https://taplink.cc/vnd'))
builder_inline.add(url_button, webapp_button)




