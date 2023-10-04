import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('TOKEN')
DB_NAME = os.getenv('DB_NAME')

