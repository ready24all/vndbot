import sqlite3
from config import DB_NAME


# TABLE SELECT
with sqlite3.connect(DB_NAME) as sql_conn:
    sql_request = "SELECT * FROM DAY_RATE ORDER BY timestamp DESC LIMIT 1"
    sql_cursor = sql_conn.execute(sql_request)
    records = sql_cursor.fetchall()
    rec_last = records[0]

usdt_to_vnd = records[0][1]
usd_to_vnd = records[0][2]
rub_to_vnd = records[0][3]

def print_rate():
    with sqlite3.connect(DB_NAME) as sql_conn:
        sql_request = "SELECT * FROM DAY_RATE ORDER BY timestamp DESC LIMIT 1"
        sql_cursor = sql_conn.execute(sql_request)
        records = sql_cursor.fetchall()
        rate = f"\n🔵Актуальный курс на {records[0][0]}\n🌐 100 USDT - {records[0][1]*100} VND\
      \n💲 100 USD - {records[0][2]*100} VND\n💰 10 000 RUB - {records[0][3]*10000} VND"
        return rate


with sqlite3.connect(DB_NAME) as sql_conn:
    sql_request = "PRAGMA table_info(DAY_RATE)"
    sql_cursor = sql_conn.execute(sql_request)
    records = sql_cursor.fetchall()
   
   
import sqlite3
def sql_get_currency(curr, db='vnd.db'):
    with sqlite3.connect(db) as sql_conn:
        sql_request = f"SELECT {curr} FROM DAY_RATE ORDER BY timestamp DESC LIMIT 1"
        sql_cursor = sql_conn.execute(sql_request)
        record = sql_cursor.fetchone()[0]
        return record

# print(sql_get_currency('RUB'))
# print(sql_get_currency('USD'))
# print(sql_get_currency('USDT'))
