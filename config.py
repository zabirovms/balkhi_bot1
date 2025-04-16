import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Token
BOT_TOKEN = os.getenv("7841345426:AAHXmUG_PwDhPOP1iqXDN2lqNBvlysLINsk")

# PostgreSQL Database Configuration
DB_CONFIG = {
    "dbname": os.getenv("potgres"),
    "user": os.getenv("zabirovms"),
    "password": os.getenv("anas171801"),
    "host": os.getenv("localhost"),
    "port": os.getenv("5432")
}
