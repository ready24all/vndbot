import sqlite3

DB_NAME = 'vnd.db'

# TABLE CREATION
with sqlite3.connect(DB_NAME) as sql_conn:
    sql_request = """CREATE TABLE IF NOT EXISTS DAY_RATE (
        date date,
        USDT integer NOT NULL,
        USD integer NOT NULL,
        RUB integer NOT NULL
    );"""
sql_conn.execute(sql_request)

# TABLE INSERT
# with sqlite3.connect(DB_NAME) as sql_conn:
#     sql_request = "INSERT INTO DAY_RATE VALUES(?, ?, ?, ?)"
#     sql_conn.execute(sql_request, ('1991-12-22', 23000, 23000, 231))
#     sql_conn.commit()


# TABLE SELECT
# with sqlite3.connect(DB_NAME) as sql_conn:
#     sql_request = "SELECT * FROM DAY_RATE ORDER BY date DESC LIMIT 1"
#     sql_cursor = sql_conn.execute(sql_request)
#     records = sql_cursor.fetchall()
#     rec_last = records[0]
#     print(rec_last[0])
#     print(records[0])

# rate = f"\n🔵Актуальный курс на {records[0][0]}\n🌐 100 USDT - {records[0][1]*100} VND\
#       \n💲 100 USD - {records[0][2]*100} VND\n💰 10 000 RUB - {records[0][3]*10000} VND"

