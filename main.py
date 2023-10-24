import asyncio
import logging
import sys
from create_bot import bot, dp
from handlers import command_start_handler, message_handler_command_kb, callback_query_picture, message_handler_inline_kb, message_get_rate, message_remove_kb, message_handler_mersi
from adminrate import message_handler_rate, message_handler_rate2, insert_rate
from calc import command_calc, process_currency, wrong_amount, process_amount



async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    logging.info("bot was initialized")
    # And the run events dispatching
    await dp.start_polling(bot)



if __name__ == "__main__":
    # logging.basicConfig(filename='logs.log', level=logging.DEBUG,
    #         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logging.basicConfig(level=logging.INFO, stream=sys.stdout,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    asyncio.run(main())