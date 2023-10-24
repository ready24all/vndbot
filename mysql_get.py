import mysql.connector
from config import DB_CONFIG


# TABLE SELECT

with mysql.connector.connect(**DB_CONFIG) as db_connection:
    with db_connection.cursor() as cursor:
        cursor.execute("SELECT * FROM DAY_RATE ORDER BY timestamp DESC LIMIT 1")
        records = cursor.fetchall()
        # print(records)

usdt_to_vnd, usd_to_vnd, rub_to_vnd = records [0][2:5]
# print(usdt_to_vnd, usd_to_vnd, rub_to_vnd)

def print_rate():
    with mysql.connector.connect(**DB_CONFIG) as db_connection:
        with db_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM DAY_RATE ORDER BY timestamp DESC LIMIT 1")
            records = cursor.fetchall()
            rate = f"\n🔵Актуальный курс на {records[0][1]}\n🌐 100 USDT - {records[0][2]*100} VND\
        \n💲 100 USD - {records[0][3]*100} VND\n💰 10 000 RUB - {records[0][4]*10000} VND"
            return rate
   
   
def sql_get_currency(curr):
    with mysql.connector.connect(**DB_CONFIG) as db_connection:
        with db_connection.cursor() as cursor:
            sql_request = f"SELECT {curr} FROM DAY_RATE ORDER BY timestamp DESC LIMIT 1"
            cursor.execute(sql_request)
            record = cursor.fetchone()[0]
            return record
    








