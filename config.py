import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')


DB_CONFIG = {
    'host': 'mysql',
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
    'database': os.getenv('DB_NAME'),
}