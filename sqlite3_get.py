import sqlite3

DB_NAME = 'vnd.db'

# TABLE SELECT
with sqlite3.connect(DB_NAME) as sql_conn:
    sql_request = "SELECT * FROM DAY_RATE ORDER BY date DESC LIMIT 1"
    sql_cursor = sql_conn.execute(sql_request)
    records = sql_cursor.fetchall()
    rec_last = records[0]
    # print(rec_last[0])
    # print(records[0])

rate = f"\n🔵Актуальный курс на {records[0][0]}\n🌐 100 USDT - {records[0][1]*100} VND\
      \n💲 100 USD - {records[0][2]*100} VND\n💰 10 000 RUB - {records[0][3]*10000} VND"

usdt_to_vnd = records[0][1]
usd_to_vnd = records[0][2]
rub_to_vnd = records[0][3]

