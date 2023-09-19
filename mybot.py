import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from config import TOKEN

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

my_router = Router(name=__name__)

@my_router.message(F.text == 'heyhey')
async def message_handler111(message: Message):
    await message.answer('Hello from my router!')

@my_router.message(F.text.regexp(r"^(\d+)$").as_("digits"))
async def any_digits_handler(message: Message):
    await message.answer('Hello from my router22222222')
# builder = InlineKeyboardBuilder()
# for index in range(1, 3):
#     builder.button(text=f"Set {index}", callback_data=f"set:{index}")
# builder.adjust(3, 2)

builder = ReplyKeyboardBuilder()
builder.button(text='Test Button1', callback_data='button pushed').adjust(1)
builder.button(text='Test Button2', callback_data='button pushed').adjust(1)
builder.button(text='Test Button3', callback_data='button pushed').adjust(1)
# builder.adjust(1, 1, 1)

@dp.message(Command("kill"))
async def test_handler(message: Message) -> None:
    await message.answer(f"Test kills", reply_markup=builder.as_markup())



@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    print('here\n')
    print(Message)
    print(type(Message))
    print('\nhere')
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


# @dp.message(filters='Test Button1')
# async def echo_handler(message: types.Message) -> None:
#     await message.answer(f"Button pressed")
#     # try:
#     #     # Send a copy of the received message
#     #     await message.send_copy(chat_id=message.chat.id)
#     # except TypeError:
#     #     # But not all the types is supported to be copied so need to handle it
#     #     await message.answer("Nice try!")




async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())