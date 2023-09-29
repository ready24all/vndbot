from sqlite3_get import *
print(type(rate))
print(rub_to_vnd)

marker = 'rub'
usdt_to_vnd
usd_to_vnd 
rub_to_vnd 

@my_router.callback_query(F.text.lower().in_({'usdt', 'usd', 'rub'}))
async def callback_query_handler(call):
    await call.message.answer('Введите сумму:')
    marker = F.data
    return marker

@my_router.message(F.text.regexp(r"^(\d+)$").as_("digits"))
async def any_digits_handler(message):
    await message.answer('Hello from my digits')
    amount = F.data
    if marker == 'usdt':
        money_res = usdt_to_vnd * amount
    elif marker == 'usd':
        money_res = usd_to_vnd * amount
    else:
        money_res = rub_to_vnd * amount
    await message.answer(f'Hello from my digits: {money_res}')


@my_router.callback_query(F.data == 'usdt')
async def callback_query_handler(call):
    await call.message.answer(call.data)
    await call.message.answer('f1 data test')
    marker = F.data

@my_router.callback_query(F.data == 'usd')
async def callback_query_handler(call):
    await call.message.answer(call.data)
    await call.message.answer('f1 data test')

@my_router.callback_query(F.data == 'rub')
async def callback_query_handler(call):
    await call.message.answer(call.data)
    await call.message.answer('f1 data test')



