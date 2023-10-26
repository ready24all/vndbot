import mysql.connector
from config import DB_CONFIG


with mysql.connector.connect(**DB_CONFIG) as db_connection:
    with db_connection.cursor() as cursor:
        sql_request = """CREATE TABLE IF NOT EXISTS DAY_RATE (
            id INT AUTO_INCREMENT PRIMARY KEY,
            DATE DATE,
            USDT INT NOT NULL,
            USD INT NOT NULL,
            RUB INT NOT NULL,
            TIMESTAMP TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );"""

        cursor.execute(sql_request)
    db_connection.commit()


from datetime import datetime
rate_list = [datetime.now().strftime("%Y-%m-%d"), 23900, 23900, 241, datetime.now()]



with mysql.connector.connect(**DB_CONFIG) as db_connection:
    with db_connection.cursor() as cursor:
        sql_request = "INSERT INTO DAY_RATE (DATE, USDT, USD, RUB, TIMESTAMP) VALUES (%s, %s, %s, %s, %s)"
        # sql_request = "INSERT INTO DAY_RATE (date, USDT, USD, RUB) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql_request, rate_list)
    db_connection.commit()
    # with db_connection.cursor() as cursor:
    #     # sql_request = "SET GLOBAL time_zone = '+07:00';"
    #     cursor.execute(sql_request)

